class Aluno():
    def __init__(self, nome, nota1, nota2):
        self.nome = nome
        self.nota1 = nota1
        self.nota2 = nota2
    
    def calcular_media(self):
        return (self.nota1 + self.nota2)/2

Aluno1 = Aluno('Bruno', 7, 7)
print(Aluno1.calcular_media())