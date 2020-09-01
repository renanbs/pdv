from marshmallow import fields, Schema, post_load, ValidationError
from pycpfcnpj import cpfcnpj
from pycpfcnpj.compatible import clear_punctuation

from pdv.repository.establishment_model import Establishment


def validate_cnpj(cnpj):
    if not cpfcnpj.validate(cnpj):
        raise ValidationError('Invalid CNPJ')


class EstablishmentSchema(Schema):
    cnpj = fields.Str(validate=validate_cnpj)
    nome = fields.Str()
    dono = fields.Str()
    telefone = fields.Str()

    @post_load
    def make_establishment(self, data, **kwargs):
        data['cnpj'] = clear_punctuation(data['cnpj'])
        return Establishment(**data)
