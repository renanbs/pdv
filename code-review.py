# CODE REVIEW:  python 3 não precisa deste encode
# -*- coding: utf-8 -*-

# CODE REVIEW: remover imports não usados (traceback, timedelta, timezone)
import os, sys, traceback, logging, configparser
import xlsxwriter
from datetime import datetime, timedelta, timezone
from apscheduler.schedulers.blocking import BlockingScheduler
from flask import Flask
from flask_sqlalchemy import SQLAlchemy
from logging.handlers import RotatingFileHandler


# CODE REVIEW: remover argv se nao for usar os parametros de linha de comando
def main(argv):
    greetings()

    print('Press Crtl+{0} to exit'.format('Break' if os.name == 'nt' else 'C'))

    # CODE REVIEW: pra que precisa do flask se nao tem api?
    app = Flask(__name__)
    # CODE REVIEW: Melhor setar o logger apropriadamente
    handler = RotatingFileHandler('bot.log', maxBytes=10000, backupCount=1)
    handler.setLevel(logging.INFO)
    app.logger.addHandler(handler)
    # CODE REVIEW: Usar variaveis de ambiente pra não expor dados de segurança do banco
    app.config['SQLALCHEMY_DATABASE_URI'] = 'postgresql+psycopg2://postgres:123mudar@127.0.0.1:5432/bot_db'
    db = SQLAlchemy(app)
    config = configparser.ConfigParser()
    # CODE REVIEW: Lendo as configurações do projeto de um diretório temporário?
    config.read('/tmp/bot/settings/config.ini')

    var1 = int(config.get('scheduler','IntervalInMinutes'))
    app.logger.warning('Intervalo entre as execucoes do processo: {}'.format(var1))
    scheduler = BlockingScheduler()

    task1_instance = scheduler.add_job(task1(db), 'interval', id='task1_job', minutes=var1)

    try:
        scheduler.start()
    except(KeyboardInterrupt, SystemExit):
        pass


def greetings():
    print('             ##########################')
    print('             # - ACME - Tasks Robot - #')
    print('             # - v 1.0 - 2020-07-28 - #')
    print('             ##########################')


# CODE REVIEW: dar um nome mais significativo, que indique o que a task está fazendo
def task1(db):
    file_name = 'data_export_{0}.xlsx'.format(datetime.now().strftime("%Y%m%d%H%M%S"))
    file_path = os.path.join(os.path.curdir, file_name)
    workbook = xlsxwriter.Workbook(file_path)
    worksheet = workbook.add_worksheet()

    orders = db.session.execute('SELECT * FROM users;')

    index = 1
    worksheet.write('A{0}'.format(index),'Id')
    worksheet.write('B{0}'.format(index),'Name')
    worksheet.write('C{0}'.format(index),'Email')
    worksheet.write('D{0}'.format(index),'Password')
    worksheet.write('E{0}'.format(index),'Role Id')
    worksheet.write('F{0}'.format(index),'Created At')
    worksheet.write('G{0}'.format(index),'Updated At')

    for order in orders:
        index = index + 1

        # CODE REVIEW: pode remover todos os prints dentro deste loop
        print('Id: {0}'.format(order[0]))
        worksheet.write('A{0}'.format(index),order[0])
        print('Name: {0}'.format(order[1]))
        worksheet.write('B{0}'.format(index),order[1])
        print('Email: {0}'.format(order[2]))
        worksheet.write('C{0}'.format(index),order[2])
        print('Password: {0}'.format(order[3]))
        # CODE REVIEW: remover print de dados sensiveis
        worksheet.write('D{0}'.format(index),order[3])
        print('Role Id: {0}'.format(order[4]))
        worksheet.write('E{0}'.format(index),order[4])
        print('Created At: {0}'.format(order[5]))
        worksheet.write('F{0}'.format(index),order[5])
        print('Updated At: {0}'.format(order[6]))
        worksheet.write('G{0}'.format(index),order[6])

    workbook.close()
    print('job executed!')


if __name__ == '__main__':
    # CODE REVIEW: remover sys.argv se nao for usar os parametros de linha de comando
    main(sys.argv)
