import sys

iterable = ['Eu', 'Tenho', '_iter_']
iterator = iter(iterable)
lista = [n for n in range(100000)]
generator = (n for n in range(100000))

print(sys.getsizeof(lista)),print('Bytes'),print()
print(sys.getsizeof(generator)),print('Bytes'),print()

print(next(generator))

for n in generator:
    print(n)