import sys
argumento_1 = input("Digite seu primeiro argumento: ")
argumento_2 = input ("Digite seu segundo argumento: ")

try:
    argumento_1_int = int(argumento_1)
    argumento_2_int = int(argumento_2)
except ValueError:
    print("Digite um número inteiro.")
    sys.exit()
soma_1 = argumento_1_int
soma_2 = argumento_2_int
resultado = argumento_1_int * argumento_2_int
print(argumento_1_int * argumento_2_int)
if resultado % 2 == 0:
    print ("O resultado é par.")
else:
    print ("O número é impar.")