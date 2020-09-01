from marshmallow import fields, Schema, post_load, ValidationError
from pycpfcnpj import cpfcnpj

from pdv.repository.transaction_model import Transaction


def validate_cpf_cnpj(cpf):
    if not cpfcnpj.validate(cpf):
        raise ValidationError('Invalid cpf')


class TransactionSchema(Schema):
    cliente = fields.Str(validate=validate_cpf_cnpj)
    descricao = fields.Str()
    estabelecimento = fields.Str(validate=validate_cpf_cnpj)
    valor = fields.Decimal(as_string=True)

    @post_load
    def make_transaction(self, data, **kwargs):
        data['cliente'] = data['cliente'].replace('.', '').replace('/', '').replace('-', '')
        data['estabelecimento'] = data['estabelecimento'].replace('.', '').replace('/', '').replace('-', '')
        return Transaction(**data)


