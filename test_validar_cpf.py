import unittest
from validar_cpf import validar_cpf
class TestValidarCPF(unittest.TestCase):

    def test_cpf_valido(self):
        self.assertTrue(validar_cpf('11718625750'))

    def test_cpf_invalido_digitos_iguais(self):
        self.assertFalse(validar_cpf('11111111111'))

    def test_cpf_invalido_com_letras(self):
        self.assertFalse(validar_cpf('abc12345678'))

    def test_cpf_invalido_com_caracteres_especiais(self):
        self.assertFalse(validar_cpf('123.456.789-00'))

    def test_cpf_invalido_com_menos_digitos(self):
        self.assertFalse(validar_cpf('1234567890'))

    def test_cpf_invalido_com_mais_digitos(self):
        self.assertFalse(validar_cpf('123456789012'))

    def test_cpf_invalido_digito_verificador(self):
        self.assertFalse(validar_cpf('11718625751'))

if __name__ == '__main__':
    unittest.main()