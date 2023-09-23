lista = []
tot = 0
print('Informe 5 números:')
for i in range(5):
    num = float(input(f'{i+1}: '))
    lista.append(num)

for i in lista:
    if i % 2 == 0:
        tot += i

media = tot / len(lista)

print(f'A média dos números pares é: {media}')
    