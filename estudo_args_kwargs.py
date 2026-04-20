def pedir_pizza(tamanho, *coberturas, **detalhes):
    print (f'Uma pizza de tamanho {tamanho} solicitada')

    print("Com as seguintes coberturas:")
    for cobertura in coberturas:
        print(f"-{cobertura}")

        print("\nCom os seguintes detalhes: ")
        for chave, valor in detalhes.items():
            print(f"-{chave}:{valor}")

pedir_pizza("grande", "Calabresa", "Tomate", "Queijo", "Oregano", entrega = True, gorjeta = 15)