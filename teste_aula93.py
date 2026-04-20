try:
    a = input('Digite um número: ')
    a_int = int(a)
except Exception as e:
    print(e.__class__.__name__)
    print(e)