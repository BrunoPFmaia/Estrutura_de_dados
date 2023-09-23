import random

opcoes = ['pedra', 'papel', 'tesoura']
maquina = opcoes[random.randint(0,2)]
msg = None

while msg == None:
    print('==============================')
    jogador = input('Pedra, papel ou tesoura? ')

    if jogador == maquina:
        msg = 'empatou!'
    elif jogador == 'pedra' and maquina == 'tesoura':
        msg = 'venceu! =)'
    elif jogador == 'pedra' and maquina == 'papel':
        msg = 'perdeu! =('

    elif jogador == 'papel' and maquina == 'pedra':
        msg = 'venceu! =)'
    elif jogador == 'papel' and maquina == 'tesoura':
        msg = 'perdeu! =('

    elif jogador == 'tesoura' and maquina == 'pedra':
        msg = 'perdeu! =('
    elif jogador == 'tesoura' and maquina == 'papel':
        msg = 'venceu! =)'

    else:
        print('Opção inválida! tente novamente.')

print(f'Resultado: {jogador} X {maquina}')
print(f'Você {msg}')