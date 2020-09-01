from pycpfcnpj import cpfcnpj
from pycpfcnpj.compatible import clear_punctuation


class SerializerException(Exception):
    pass


class Serializer:
    def __init__(self, cnpj: str):
        self._cnpj = cnpj

    def _has_cnpj_field(self):
        if not self._cnpj:
            raise SerializerException('cnpj filter is required')

    def _has_a_valid_cnpj(self):
        if not cpfcnpj.validate(self._cnpj):
            raise SerializerException('invalid cnpj')

    def is_valid(self):
        self._has_cnpj_field()
        self._has_a_valid_cnpj()

    @property
    def cnpj(self):
        return clear_punctuation(self._cnpj)
