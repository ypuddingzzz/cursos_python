
try:
    numero_inteiro = int(input("Digite um número inteiro: "))
    print(f"O número {numero_inteiro} é um número inteiro.")
except ValueError:
    print("O valor digitado não é um número inteiro.")
    quit()
if numero_inteiro % 2 == 0:
    print(f"O número {numero_inteiro} é par.")
else:    print(f"O número {numero_inteiro} é ímpar.")


horas = input('Que horas são? ')

try:
    horas = int(horas)
except ValueError:
    print("Hora inválida. Por favor, insira uma hora válida no formato HH:MM.")
    quit()

if horas  >= 0 and horas <= 11:
        print ("Bom dia!")
elif horas >= 12 and horas < 18:
        print ("Boa tarde!")
elif horas >= 19 and horas < 24:
        print ("Boa noite!")
elif horas >= 25 or horas < 0:
        print ('Hora inválida. Por favor, insira uma hora válida no formato "H".') 
        quit()

nome = input('Digite seu nome: ')
if len(nome) < 4:
    print(f'Seu nome é curto.')
elif len(nome) >= 5 and len(nome) <= 6:
    print(f'Seu nome é normal.') 
else:
    print(f'Seu nome é muito grande.')
