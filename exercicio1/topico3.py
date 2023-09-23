num = int(input('Informe um número: '))

print('os números pares são:')
for i in range(0,num+1):
    if i % 2 == 0:
        print(i)