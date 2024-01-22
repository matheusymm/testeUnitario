import math
import unittest

class MetabolismoBasal():
    def __init__(self, fatAtividade, peso, altura, idade, genero):
        self.fatAtividade = fatAtividade
        self.peso = peso
        self.altura = altura
        self.idade = idade
        self.genero = genero
    
    def calcMasc(self):
        return math.ceil(self.fatAtividade*(66 + 13.7*self.peso + 5*self.altura - 6.8*self.idade))
    
    def calcFem(self):
        return math.ceil(self.fatAtividade*(655 + 9.6*self.peso + 1.8*self.altura - 4.7*self.idade))
    
class TesteClass(unittest.TestCase):
    def testeMascSedentario(self):
        TMB = MetabolismoBasal(1.2, 60, 170, 24, 0)
        self.assertEqual(1890, TMB.calcMasc(), "Masculino Sedentário Falhou!")
    def testeMascModeradamenteAtivo(self):
        TMB = MetabolismoBasal(1.55, 60, 170, 24, 0)
        self.assertEqual(2441, TMB.calcMasc(), "Masculino Moderadamente Ativo Falhou!")
    def testeMascAltamenteAtivo(self):
        TMB = MetabolismoBasal(1.725, 60, 170, 24, 0)
        self.assertEqual(2717, TMB.calcMasc(), "Masculino Sedentário Falhou!")
    def testeFemSedentario(self):
        TMB = MetabolismoBasal(1.2, 60, 170, 24, 1)
        self.assertEqual(1710, TMB.calcFem(), "Feminino Sedentário Falhou!")
    def testeFemModeradamenteAtivo(self):
        TMB = MetabolismoBasal(1.55, 60, 170, 24, 1)
        self.assertEqual(2208, TMB.calcFem(), "Feminio Moderadamente Ativo Falhou!")
    def testeFemAltamenteAtivo(self):
        TMB = MetabolismoBasal(1.725, 60, 170, 24, 1)
        self.assertEqual(2457, TMB.calcFem(), "Feminino Altamente Ativo Falhou!")

if __name__ == "__main__":
    unittest.main()