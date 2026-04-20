import subprocess

lista = []
valor = ""
while True:
    print('Selecione uma opção:')
    opcoes = input('[i]nserir [a]pagar [l]istar ')
    subprocess.run("cls", shell=True)
    
    if opcoes == "i":
       valor = input('Valor: ')
    lista.append(valor)
    subprocess.run("cls", shell=True)


    if opcoes == "a":
            apagar = input("Qual valor você deseja apagar?: ")
            if apagar in valor in enumerate(lista):
                del valor
                print("Valor apagado.")
            else: print("Digite um valor existente.")
    
            for indice, nome in enumerate(lista):
                del indice
                print("Valor apagado.")

    if opcoes == "l":
        if valor == "":
             print("Não há valores")
        for indice, valor in enumerate(lista):
            print(f'[{indice}] {valor}')
        input()
        subprocess.run("cls", shell=True)

