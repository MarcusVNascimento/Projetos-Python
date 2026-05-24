#                      CALCULADORA BÁSICA

num1 = int(input("Digite um número: \n"))

num2 = int(input("Digite o outro número: \n"))

op = input("escolha seu operador: \n")

if op == '*':
    print(num1 * num2)
elif op == '/':
    print(num1 / num2)
elif op == '+':
    print(num1 + num2)
elif op == '-':
    print(num1 - num2)
else:
    print("Escolha um operadorr válido!")