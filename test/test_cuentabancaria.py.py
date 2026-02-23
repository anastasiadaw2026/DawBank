import unittest
from lib.cuenta_bancaria import CuentaBancaria

class MyTestCase(unittest.TestCase):
    def test_iban_correcto(self):
        iban1 = "ES1234567890123456789012"
        self.cuenta = CuentaBancaria(iban1,'A B')
        self.assertEqual(self.cuenta.iban, iban1)

    def test_iban_letra_inicial_invalida(self):
        iban_invalido = "1S1234567890123456789012"
        self.cuenta = CuentaBancaria(iban_invalido,'A B')
        self.assertIsNone(self.cuenta.iban)

    def test_iban_letra_segunda_invalida(self):
        iban_invalido = "S&1234567890123456789012"
        self.cuenta = CuentaBancaria(iban_invalido,'A B')
        self.assertIsNone(self.cuenta.iban)

    def test_iban_con_letras_en_numeros(self):
        iban_invalido = "ES12A4567890123456789012"
        self.cuenta = CuentaBancaria(iban_invalido,'A B')
        self.assertIsNone(self.cuenta.iban)

    def test_iban_longitud_corta(self):
        iban_invalido = "ES123"
        self.cuenta = CuentaBancaria(iban_invalido,'A B')
        self.assertIsNone(self.cuenta.iban)

    def test_iban_longitud_larga(self):
        iban_invalido = "ES1234567890123456789012345"
        self.cuenta = CuentaBancaria(iban_invalido,'A B')
        self.assertIsNone(self.cuenta.iban)

if __name__ == '__main__':
    unittest.main()
