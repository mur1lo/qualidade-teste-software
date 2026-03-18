import unittest
from ecommerce import calcular_desconto


class TestQualidade(unittest.TestCase):

    def test_aplica_frete_quando_total_pos_desconto_fica_abaixo_de_150(self):
        cupom = ""
        resultado = calcular_desconto(100, cupom)
        self.assertEqual(resultado, 105.0)

    def test_aplica_cupom_quero20_e_cobra_frete_quando_total_fica_abaixo_do_limite(self):
        cupom = "QUERO20"
        resultado = calcular_desconto(50, cupom)
        self.assertEqual(resultado, 55.0)

    def test_compra_de_100_reais_resulta_em_105_com_desconto_e_frete(self):
        cupom = ""
        resultado = calcular_desconto(100, cupom)
        self.assertEqual(resultado, 105.0)

    def test_cupom_off50_valido_para_compra_acima_de_600(self):
        cupom = "OFF50"
        resultado = calcular_desconto(800, cupom)
        self.assertEqual(resultado, 400.0)

    def test_cupom_off50_invalido_aplica_regra_padrao_de_10_porcento(self):
        cupom = "OFF50"
        resultado = calcular_desconto(200, cupom)
        self.assertEqual(resultado, 180.0)

if __name__ == '__main__':
    unittest.main()