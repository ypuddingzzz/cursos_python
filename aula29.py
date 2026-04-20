numero_str = input("Vou dobrar o número que você digitar. Digite um número: ")

try:
    numero_float = float(numero_str)
    print ('FLOAT ', numero_float)
    print(f"O dobro de {numero_str} é {numero_float * 2:.2f}.") 
except:
    print ("O valor digitado não é um número.")