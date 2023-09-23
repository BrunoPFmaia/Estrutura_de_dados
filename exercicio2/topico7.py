class Carro():
    def __init__(self, marca, modelo, ano):
        self.marca = marca
        self.modelo = modelo
        self.ano = ano
    
    def detalhes(self):
        print(f'Marca: {self.marca}, Modelo: {self.modelo}, Ano: {self.ano}')

Carro1 = Carro('Chevrollet', 'Camaro', '78')
Carro1.detalhes()