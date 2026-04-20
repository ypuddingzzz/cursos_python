palavra_secreta = "tetano"
letras_acertadas = ''
numero_tentativas = 0

while True:
    letra_digitada = input("Digite uma letra: ")
    numero_tentativas += 1

    if len(letra_digitada) > 1:
        print ("Digite apenas uma letra:")
    if letra_digitada in palavra_secreta:
        letras_acertadas += letra_digitada

    palavra_nova = ''
    for letra_secreta in palavra_secreta:
        if letra_secreta in letras_acertadas:
            palavra_nova += letra_secreta
        else:
            palavra_nova += "*"

    print(palavra_nova)

    if palavra_nova == palavra_secreta:
        print('Você ganhou.')
        print(f'Você errou {numero_tentativas - 1}x.')
        quit()