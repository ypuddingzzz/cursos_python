print('num')
sair = input ('Quer sair?: [s]im: ').lower().startswith('s')
while sair == False:
    numero_1 = input ('Digite um número: ')
    
    try:
        num_1_float = float(numero_1)
    except:
        print("O número digitado não é válido.")
        continue
    
    numero_2 = input ('Digite outro número: ')

    try:
        num_2_float = float(numero_2)
    except:
        print("O número digitado não é válido.")
        continue
    
    operador = input ('Digite o operador (+-/*) ')
    
    if operador == "+":
            print ("Realizando sua conta. Confira o resultado abaixo:")
            resultado = num_1_float + num_2_float
            print (f'{num_1_float} "+" {num_2_float} == {resultado}')

    elif operador == "-":
            print ("Realizando sua conta. Confira o resultado abaixo:")
            resultado = num_1_float - num_2_float
            print (f'{num_1_float} "-" {num_2_float} == {resultado}')

    elif operador == "/":
            
            print ("Realizando sua conta. Confira o resultado abaixo:")
            resultado = num_1_float + num_2_float
            print (f'{num_1_float} "/" {num_2_float} == {resultado}')         

    elif operador == "*":
            print ("Realizando sua conta. Confira o resultado abaixo:")
            resultado = num_1_float + num_2_float
            print (f'{num_1_float} "*" {num_2_float} == {resultado}')

    else:
            print("Operador inválido.")
            continue
    
    sair = input ('Quer sair?: [s]im: ').lower().startswith('s')
    if sair is True:
        quit()

    
    if sair is True:
        break