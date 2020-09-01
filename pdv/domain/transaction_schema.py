from marshmallow import fields, Schema, post_load, ValidationError
from pycpfcnpj import cpfcnpj
from pycpfcnpj.compatible import clear_punctuation

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
        data['cliente'] = clear_punctuation(data['cliente'])
        data['estabelecimento'] = clear_punctuation(data['estabelecimento'])
        return Transaction(**data)
