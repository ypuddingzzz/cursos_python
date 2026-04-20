nome = input ('Digite seu nome: ')
if nome.isdigit():
    print ("Nome inválido. Por favor, insira um nome que contenha apenas letras.")
    quit()
if nome.strip() == "":
    print ("Desculpe, você deixou campos vazios.")
    quit()
idade = input ('Digite sua idade: ')
if idade.isdigit() == False:
    print ("Desculpe,você deixou campos vazios.")
    quit()

print ("seu nome é: ", nome)
print ("seu nome invertido é: ", nome[::-1])
print ("seu nome contém (ou não) espaços ", " " in nome)
print ("a primeira letra do seu nome é: ", nome[0])
print ("a última letra do seu nome é: ", nome[-1])