
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

if ":" not in horas:
    print ("Hora inválida. Por favor, insira uma hora válida no formato HH:MM.")
    quit()
hora_min = horas.split(':')
if len(hora_min) != 2 or not hora_min[0].isdigit() or not hora_min[1].isdigit():
    print ("Hora inválida. Por favor, insira uma hora válida no formato HH:MM.")
    quit()

hora_int = int(hora_min[0])
minuto_int = int(hora_min[1])

if hora_int < 0 or hora_int >= 24 or minuto_int < 0 or minuto_int >= 60:
    print ("Hora inválida. Por favor, insira uma hora válida no formato HH:MM.")
    quit()

hora_part, minuto_part = horas.split(':')
if not (hora_part.isdigit() and minuto_part.isdigit()):
    print("Hora inválida. Por favor, insira uma hora válida no formato HH:MM.")
    quit()

hora_int = int(hora_part)
minuto_int = int(minuto_part)

if hora_int < 0 or hora_int >= 24 or minuto_int < 0 or minuto_int >= 60:
    print("Hora inválida. Por favor, insira uma hora válida no formato HH:MM.")
    quit()

horas = int(horas.split(':')[0])  # Converte a hora para um inteiro

if horas  >= 0 and horas <= 12:
        print ("Bom dia!")
elif horas >= 12 and horas < 18:
        print ("Boa tarde!")
elif horas >= 18 and horas < 24:
        print ("Boa noite!")
elif horas >= 24 or horas < 0:
        print ("Hora inválida. Por favor, insira uma hora válida no formato HH:MM.") 
        quit()
elif not (len(horas) == 4 and ":" in horas):
        print("Hora inválida. Por favor, insira uma hora válida no formato HH:MM.")
        quit()

nome = input('Digite seu nome: ')
if len(nome) < 4:
    print(f'Seu nome é curto.')
elif len(nome) >= 5 and len(nome) <= 6:
    print(f'Seu nome é normal.') 
else:
    print(f'Seu nome é muito grande.')
