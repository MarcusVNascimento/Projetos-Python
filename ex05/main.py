import random

lista = []

soma = 0

for i in range(9):
    item = random.randint(0,9)
    lista.append(item)

it = 10

for num in lista:
    mult = num * it
    soma += mult
    it -= 1

result = (soma * 10) % 11
result = result if result <= 9 else 0





lista.append(result)

it = 11
soma = 0

for num in lista:
    mult = num * it
    soma += mult
    it -= 1

resultado = (soma * 10) % 11
resultado = resultado if resultado <= 9 else 0

lista.append(resultado)
cpf = ''.join(map(str, lista))

print(f'O CPF gerado é: {cpf}')

