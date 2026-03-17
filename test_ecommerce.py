import unittest
from ecommerce import calcular_desconto


class TestQualidade(unittest.TestCase):

    def test_desconto_cupom(self):
        cupom = "QUERO20"
        resultado = calcular_desconto(200, cupom)
        self.assertEqual(resultado, 160.0)

    def test_desconto_preco(self):
        cupom = ""
        resultado = calcular_desconto(150, cupom)
        self.assertEqual(resultado, 150.0)

    def test_cenario_frete(self):
        cupom = ""
        resultado = calcular_desconto(100, cupom)
        self.assertEqual(resultado, 105.0)

    def test_cenario_cupom_valido(self):
        cupom = "OFF50"
        resultado = calcular_desconto(800, cupom)
        self.assertEqual(resultado, 400.0)

    def test_cenario_cupom_invalido(self):
        cupom = "OFF50"
        resultado = calcular_desconto(200, cupom)
        self.assertEqual(resultado, 180.0)

if __name__ == '__main__':
    unittest.main()