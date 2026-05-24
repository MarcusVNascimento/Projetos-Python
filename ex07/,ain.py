# Métodos úteis dos dicionários em Python
# len - quantas chaves
# keys - iterável com as chaves
# values - iterável com os valores
# items - iterável com chaves e valores
# setdefault - adiciona valor se a chave não existe
# copy - retorna uma cópia rasa (shallow copy)
# get - obtém uma chave
# pop - Apaga um item com a chave especificada (del)
# popitem - Apaga o último item adicionado
# update - Atualiza um dicionário com outro

# Exercício - sistema de perguntas e respostas


perguntas = [
    {
        'Pergunta': 'Quanto é 2+2?',
        'Opções': ['1', '3', '4', '5'],
        'Resposta': '4',
    },
    {
        'Pergunta': 'Quanto é 5*5?',
        'Opções': ['25', '55', '10', '51'],
        'Resposta': '25',
    },
    {
        'Pergunta': 'Quanto é 10/2?',
        'Opções': ['4', '5', '2', '1'],
        'Resposta': '5',
    },
]
acertos = 0
lista = []

for pergunta in perguntas:

    for item, info in pergunta.items():

        if item =='Pergunta':
            print(f'\nA pergunta é: {info}')

        if item == 'Opções':
            lista = []
            print('\nOpções: \n')

            for num, valor in enumerate(info):
                print(f'{num}) {valor}')
                lista.append(valor)

        if item == 'Resposta':
            res = input('\nResposta: ')

            try:
                responda = int(res)

            except ValueError:
                print('Você errou!')
                continue

            try:
                if lista[responda] == info:
                    print('Acertou!')
                    acertos += 1
                else:
                    print('Errou!')

            except IndexError:
                print('Você errou!')
                continue

print(f'Você acertou {acertos} de 3.')


