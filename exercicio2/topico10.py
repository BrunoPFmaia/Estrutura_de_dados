class Funcionario():
    def __init__(self, nome, salario, cargo):
        self.nome = nome
        self.salario = salario
        self.cargo = cargo
    def aumentar_salario(self, percentual):
        return self.salario + self.salario * (percentual / 100)

Funcionario1 = Funcionario('Bruno', 1000, 'Vendedor')
print(Funcionario1.aumentar_salario(10))
