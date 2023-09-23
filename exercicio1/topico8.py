def is_prime(number):
    if number <= 1:
        return False
    if number <= 3:
        return True
    if number % 2 == 0 or number % 3 == 0:
        return False
    i = 5
    while i * i <= number:
        if number % i == 0 or number % (i + 2) == 0:
            return False
        i += 6
    return True

numero = int(input("Digite um número para verificar se é primo: "))
if is_prime(numero):
    print(f"{numero} é um número primo.")
else:
    print(f"{numero} não é um número primo.")