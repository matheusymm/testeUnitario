import math
import unittest

class MetabolismoBasal():
    def __init__(self, fatAtividade, peso, altura, idade, sexo):
        self.fatAtividade = fatAtividade
        self.peso = peso
        self.altura = altura
        self.idade = idade
        self.sexo = sexo
    
    def calcHomem(self):
        return math.ceil(self.fatAtividade*(66 + 13.7*self.peso + 5*self.altura - 6.8*self.idade))
    
    def calcMulher(self):
        return math.ceil(self.fatAtividade*(655 + 9.6*self.peso + 1.8*self.altura - 4.7*self.idade))
    
class TesteClass(unittest.TestCase):
    def testeHomemSedentario(self):
        TMB = MetabolismoBasal(1.2, 60, 170, 24, 0)
        self.assertEqual(1890, TMB.calcHomem(), "Homem Sedentário Falhou!")
    def testeHomemModeradamenteAtivo(self):
        TMB = MetabolismoBasal(1.55, 60, 170, 24, 0)
        self.assertEqual(2441, TMB.calcHomem(), "Homem Moderadamente Ativo Falhou!")
    def testeHomemAltamenteAtivo(self):
        TMB = MetabolismoBasal(1.725, 60, 170, 24, 0)
        self.assertEqual(2717, TMB.calcHomem(), "Homem Sedentário Falhou!")
    def testeMulherSedentario(self):
        TMB = MetabolismoBasal(1.2, 60, 170, 24, 1)
        self.assertEqual(1710, TMB.calcMulher(), "Mulher Sedentária Falhou!")
    def testeMulherModeradamenteAtivo(self):
        TMB = MetabolismoBasal(1.55, 60, 170, 24, 1)
        self.assertEqual(2208, TMB.calcMulher(), "Mulher Moderadamente Ativa Falhou!")
    def testeMulherAltamenteAtivo(self):
        TMB = MetabolismoBasal(1.725, 60, 170, 24, 1)
        self.assertEqual(2457, TMB.calcMulher(), "Mulher Altamente Ativa Falhou!")

if __name__ == "__main__":
    unittest.main()
