class Circulo:
    def __init__(self, raio):
        self.raio = raio
    def calcular_area(self):
        return 2.14 * self.raio

circulo1 = Circulo(4)
print(circulo1.calcular_area())
