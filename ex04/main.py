lista = []

while True:
    item = input("Digite o que você deseja comprar: \n")
    if not item.isalpha():
        print("Caractere invalido, tente novamente!")
        continue
    lista.append(item)
    while True:
        vontade = input("Deseja excluir algum item da lista?\n")
        if vontade.lower() == "sim":
            delete = input("Qual item você deseja deletar?\n")
            if not delete.isalpha():
                print("Caractere invalido, tente novamente!")
                continue
            if delete not in lista:
                print("Esse item não está na lista, tente novamente!")
                continue
            lista.remove(delete)
            print("Item deletado com sucesso!")
            print(lista)
        else:
            print("Ok!")
            break
    sair = input("Deseja parar por aqui?\n")
    if sair.lower() == "sim":
        print(lista)
        print("Saindo!")
        break
