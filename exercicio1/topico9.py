lista = ['maçã', 'abacate', 'pera', 'uva', 'abacaxi']
lista_formatada = []

for elemento in lista:
    if elemento[0].lower() == 'a':
        lista_formatada.append(elemento)
print(lista_formatada)