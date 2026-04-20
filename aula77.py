# Exercício - sistema de perguntas e respostas
import sys

try:
    print("Quanto é 2+2?")    
    opcoes1 = [1, 3, 4, 5]

    print (f'Opções:', opcoes1)
    pergunta_1 = input('')

    pergunta_1_int = int(pergunta_1)

    if pergunta_1_int == 4:
        print('Acertou.✅')
    else:
        print("Você errou.❌")
        sys.exit()

except ValueError:
    print("Você errou.❌")
    sys.exit()

try:
    print("Quanto é 5*5?")
    opcoes2 = ['25', '55', '10', '51']
    
    print (f'Opções:', opcoes2)
    pergunta_2 = input('')

    pergunta_2_int = int(pergunta_2)

    if pergunta_2_int == 25:
        print('Acertou.✅')
    else:
        print("Você errou.❌")

except ValueError:
    print("Você errou.❌")
    sys.exit()

try:
    print("Quanto é 10/2?")
    opcoes3 = ['4', '5', '2', '1']

    print (f'Opções:', opcoes3)
    pergunta_3 = input('')

    pergunta_3_int = int(pergunta_3)

    if pergunta_3_int == 5:
        print('Parabéns!🥳 Você acertou todas as questões!🎉')
    else:
        print("Você errou.❌")

except ValueError:
    print("Você errou.❌")
    sys.exit()