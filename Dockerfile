FROM python:3.8.5-alpine

COPY . /app

WORKDIR /app

RUN apk add --no-cache make && make setup-dev && make setup-db

EXPOSE 5000

CMD ["python", "wsgi.py"]