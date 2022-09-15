'''class Quadrado:
        def __init__(self,lado):
            self.lado = lado
        def mostrarlado(self):
            print(self.lado)
        def trocarlado(self, outrolado):
            self.lado = outrolado
        def calculo(self):
            return self.lado ** 2'''

'''class Retangulo:
    def __init__(self, ladoA, ladoB):
        self.ladoA = ladoA
        self.ladoB = ladoB
    def mostrarladoA(self):
        print (self.ladoA)
    def mostrarladoB(self):
        print (self.ladoB)
    def trocarlado(self, outroladoA, outroladoB):
        self.ladoA = outroladoA
        self.ladoB = outroladoB
    def calculo(self):
        return self.ladoA * self.ladoB  '''

class Retangulo:
    def __init__(self, valor1, valor2):
            self.valor1 = valor1
            self.valor2 = valor2
    def mostrarvalo1(self):
            print(self.valor1)
    def mostrarvalor2(self):
            print(self.valor2)
    def calculo1(self):
        return self.valor1 * self.valor2
    def calculo2(self):
        return ((self.valor1*2)+(self.valor2*2))
   