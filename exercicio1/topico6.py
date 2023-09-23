while True:
    try:
        num = int(input('Informe um número inteiro positivo: '))
        if num < 0:
            raise ValueError('Erro: Número menor que 0')
        else:
            break
    except ValueError as e:
        print(f'Erro: {e}')

tot = num
fatorial = 0

for i in range(1,num):
    print(f'{tot} * {i}')
    fatorial = tot * i
    tot = fatorial
    print(fatorial)

print(f'O numero é {fatorial}')
