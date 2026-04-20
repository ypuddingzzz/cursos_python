cpf = [6,9,5,7,5,5,1,9,0,3,5]

zero = (cpf[0]) 
um = (cpf[1]) 
dois = (cpf[2]) 
tres = (cpf[3]) 
quatro = (cpf[4]) 
cinco = (cpf[5]) 
seis = (cpf[6]) 
sete = (cpf[7]) 
oito = (cpf[8]) 

soma = (zero * 10, um * 9, dois * 8 , tres * 7 , quatro * 6,
        cinco * 5 , seis * 4 , sete * 3 , oito * 2 )

resultado_soma = (soma[0] + soma[1] + soma[2] + soma[3] + soma[4]
                   + soma[5] + soma[6] + soma[7] + soma[8])

soma_vezes_dez = (resultado_soma * 10)

resto_soma = soma_vezes_dez % 11

if resto_soma >9:
    primeiro_digito = 0
elif resto_soma <9:
    primeiro_digito = resto_soma
else:
    print("Valor incorreto.")

print(primeiro_digito)