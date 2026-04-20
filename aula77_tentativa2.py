perguntas = [
    {
        'Pergunta': 'Qual é o nome do país que aconteceu o acidente radiológico mais famoso do mundo com césio 137?',
        'Opções': ['Rússia', 'Ucrânia', 'Brasil', 'Chernobyl'],
        'Resposta': '2',
    },
    {
        'Pergunta': 'Qual é o nome do ato da água virar gelo?',
        'Opções': ['Solidificação', 'Condensação', 'Ebulição', 'Vaporização'],
        'Resposta': '0',
    },
    {
        'Pergunta': 'Qual a lei, capítulo e artigo que defendem o personagem Bobby e a CNEN'\
        ' (Comissão Nacional de Energia Nuclear) na série "Emergência Radioativa"?',
        'Opções': ['4.118, Cap IV, Art 40.', '2.110, Cap II Art 23.', '3.541, Cap VII Art 52.', '6.521, Cap I Art 12.'],
        'Resposta': '0',
    },
]
qtd_acertos = 0

for pergunta in perguntas:
    print("Pergunta:", pergunta['Pergunta'])
    print()

    opcoes = pergunta['Opções']
    for indice, opcao in enumerate (opcoes):
        print(f'{indice})', opcao)
    print()
    
    try:
        escolha = input("Escolha uma opção: ")
        if escolha == pergunta["Resposta"]:
            print ("Você acertou!✅")
            qtd_acertos += 1
            print()
        else:
            print ("Você errou.❌")
            print()
    except ValueError: print("Você errou.❌")

    
if qtd_acertos == 3:
    print ("Meus parabéns!🥳 Você acertou todas as questões!🎉")

if qtd_acertos == 2:
    print(f'Você acertou {qtd_acertos} questões.👍 Continue assim e logo chegará em 3 acertos!✅')

if qtd_acertos == 1:
    print(f'Você acertou {qtd_acertos} questão.😊')

if qtd_acertos == 0:
    print("Você não acertou nenhuma questão.❌")