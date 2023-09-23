class Produto():
    def __init__(self, nome, preco, quantidade):
        self.nome = nome
        self.preco = preco
        self.quantidade = quantidade
    
    def calcular_total(self):
        return self.preco * self.quantidade

Produto1 = Produto('Tomate', 0.30, 10)
print(Produto1.calcular_total())