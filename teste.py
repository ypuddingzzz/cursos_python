import sys
0 == ""
nome = input ("Digite o seu nome: ")

if nome.isdigit():  
    print ("Nome inválido. Por favor, insira um nome que contenha apenas letras.")
    quit()
if nome.strip() == "":
    print ("Nome inválido. Por favor, digite seu nome.")
    quit()
altura = input ("Digite a sua altura em metros: ")

try:
    altura_float = float(altura)
    if altura_float >= 3.0 or altura_float <= 0:
        print ("Altura inválida. Por favor, insira uma altura válida entre 0 e 3 metros.")
        quit()
except ValueError:
    print ('Altura inválida. Por favor, insira uma altura válida usando "1" como formato.')
    quit()
    
peso = input ("Digite o seu peso em kg: ")

if float(peso) >= 500 or float(peso) <= 0:
    print ("Peso inválido. Por favor, insira um peso entre 0 e 500 kg.")
    quit()
elif peso.strip() == "":
    print ('Peso inválido. Por favor, insira um peso válido usando "1" como formato.')
    quit()

idade = input ("Digite a sua idade: ")

if int(idade) >= 130 or int(idade) < 1:
    print ("Idade inválida. Por favor, insira uma idade entre 1 e 130 anos.")
    quit()  
elif idade.strip() == "":
    print ('Idade inválida. Por favor, insira uma idade válida usando "1" como formato.')
    quit()

maior_de_idade = int(idade) >= 18

aniversario = input ('Fez aniversário esse ano? "sim" ou "não" ')

if aniversario == "sim":
    aniversario = 2026 - int(idade)
elif aniversario == "não":
    aniversario = 2025 - int(idade)
else:
    print ("Resposta inválida. Por favor, responda com 'sim' ou 'não'.")
    quit()

imc = float(peso) / (float(altura) ** 2)

imc_magro = imc < 18.5
imc_ideal = 18.5 <= imc < 25
imc_sobrepeso = 25 <= imc < 30
imc_obesidade = imc >= 30

print(f"Olá {nome}, sua altura é {altura}m, seu peso é {peso}kg, o senhor(a) é {('maior' if maior_de_idade else 'menor')} de idade e você fez aniversário em {aniversario}. Seu IMC é {imc:.2f}.")
if imc_magro:
    print("Você está abaixo do peso.")
elif imc_ideal:
    print("Você está com o peso ideal.")
elif imc_sobrepeso:
    print("Você está sobrepeso.")
else:
    print("Você está com obesidade.")
