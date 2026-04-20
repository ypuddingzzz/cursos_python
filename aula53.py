lista = ['Maria', 'Helena', 'Luiz']
lista.append('João')

for indice, nome in enumerate(lista):
    del indice
# for item in enumerate(lista):
#     indice, nome = item
#     print(indice, nome)

for tupla_enumerada in enumerate(lista):
    print('FOR da tupla')
    for valor in tupla_enumerada:
        print(f'{valor}')

