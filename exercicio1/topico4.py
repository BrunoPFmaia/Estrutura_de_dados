lista = []
maior_num = None
menor_num = None


print('Informe 5 números:')
for i in range(5):
    num = float(input(f'{i+1}: '))
    lista.append(num)

for i in lista:
    if maior_num == None or i > maior_num:
        maior_num = i
    if menor_num == None or i < menor_num:
        menor_num = i

print(f'menor número: {menor_num}')
print(f'maior número: {maior_num}')
