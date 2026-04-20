def potencia(base, expoente):
    return base ** expoente

def criar_funcao(funcao, *args):
    return lambda *outros_args: funcao(*args, *outros_args)
    






try:
    base_usuario = int(input("Digite uma base com um número inteiro: "))
    expoente_usuario =  int(input("digite um número inteiro para elevar o número anterior: "))
except ValueError:
    print("Digite um número inteiro.")