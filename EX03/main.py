palavra = 'marcus'
ideia = ''
resposta = ''
aparecer = ''
resposta_acertada = ''
tentativa = 0
while True:
    resposta = input('Digite uma letra: ')
    tentativa += 1
    print(f'Você esttá na tentativa {tentativa}x')
    if resposta == 'sair':
        print('Você saiu da brincadeira!')
        break
    if len(resposta) != 1:
        print('Digite uma letra!')
        continue
    if resposta in palavra:
        resposta_acertada += resposta

    aparecer = ''

    for letra in palavra:
        if letra in resposta_acertada:
            aparecer += letra
        else:
            aparecer += '*'

    print(aparecer)
    if aparecer == palavra:
        print('Parábens você acertou a palavra!')
        break
    