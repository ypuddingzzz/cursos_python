def soma(*args):
    total = 0
    for numero in args:
        print ("Total", total, numero)
        total = total + numero 
        print("Total", total)
    return total

soma1_2_3 = soma(1,2,3)
print(soma1_2_3)

