hora = int(input("Que horas são?\n"))

if hora < 0 or hora > 23:
    print("Insira uma hora válida!")
elif hora <= 11:
    print("Bom dia!")
elif hora >= 18:
    print("Boa noite!")
else:
    print("Boa tarde!")