class ContaBancaria():
    def __init__(self, saldo, titular):
        self.saldo = saldo
        self.titular = titular
    
    def depositar(self, valor):
        self.saldo += valor
    
    def sacar(self, valor):
        self.saldo -= valor

ContaBancaria1 = ContaBancaria(1000, 'Bruno Pires')
ContaBancaria1.depositar(200)
ContaBancaria1.sacar(400)
print(ContaBancaria1.saldo)