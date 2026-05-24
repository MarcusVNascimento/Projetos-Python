num = input("Digite um numero: ")

if num.isdigit():
    num_int = int(num)
    calculo = num_int % 2 == 0
    if calculo:
        print(f"O numero {num} é par")
    else:
        print(f"O numero {num} é impar")
else:
    print("Você não digitou um numero!")