##fibonacci 0 - 1 - 1 - 2 - 3 - 5 - 8

n1 = 0
n2 = 1
sequencia = []

tot = int(input("Informe um valor: "))
for i in range(tot):
    if i == 0:
        sequencia.append(n1)
    elif i == 1:
        sequencia.append(n2)
    else:
        n3 = n1 + n2
        n1 = n2
        n2 = n3
        sequencia.append(n3)
print(f"a sequencia de fiboncci até o numero informado é: {sequencia}")