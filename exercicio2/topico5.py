class Pessoa():
    def __init__(self, nome, idade):
        self.nome = nome
        self.idade = idade
    
    def falar(self):
        print(self.nome)

Pessoa1 = Pessoa('Bruno', 18)
Pessoa1.falar()