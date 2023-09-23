class Retangulo():
    def __init__(self, base, altura):
        self.base = base
        self.altura = altura
    
    def calcular_area(self):
        return self.base * self.altura

retangulo1 = Retangulo(10, 5)
print(retangulo1.calcular_area())
