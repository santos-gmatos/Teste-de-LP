import unittest
import datetime
import calculadata as dt
import modulo_leitura as ml

class DataCalculatorTest(unittest.TestCase):

    def test_1_calcular_data(self):
        self.assertEqual(dt.calcular_data("13 de Agosto de 2023 - 10 de Agosto de 2023"),(datetime.datetime(2023, 8, 10, 0, 0), datetime.datetime(2023, 8, 13, 0, 0)))
        
    def test_2_calcular_data(self):
        self.assertEqual(dt.calcular_data("13 do Agosto de 2023 - 10 blue Agosto da 2023"),ValueError)
        #O código aceita qualquer formato, desde que possua quatro inteiros e dois nomes de meses na ordem correta
        
    def test_1_calcular_diferanca(self):
        self.assertEqual(dt.calcular_diferenca(datetime.datetime(2023, 8, 10, 0, 0), datetime.datetime(2023, 8, 13, 0, 0)), "A diferenca entre as datas é de 3 dias")
        
    def test_2_calcular_diferanca(self):
        self.assertEqual(dt.calcular_diferenca(datetime.datetime(2023, 8, 13, 0, 0), datetime.datetime(2023, 8, 10, 0, 0)), "A diferenca entre as datas é de -3 dias")
        
    def test_ler_arquivo(self):
        self.assertEqual(ml.ler_arquivo("texto.txt"), "13 de agosto 2023 - 10 de agosto de 2023")
   
if __name__ == "__main__":
    unittest.main()
