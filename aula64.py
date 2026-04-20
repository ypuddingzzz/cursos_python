while True:
        import sys
        import random

        nove_digitos = ''
        for i in range(9):
            nove_digitos += str(random.randint(0,9))

        contador_regressivo_1 = 10

        resultado_digito_1 = 0
        for digito_1 in nove_digitos:
            resultado_digito_1 += int(digito_1) * contador_regressivo_1
            contador_regressivo_1 -= 1
        digito_1 = (resultado_digito_1 * 10) % 11
        digito_1 = digito_1 if digito_1 <= 9 else 0

        resultado_digito_2 = 0

        contador_regressivo_2 = 11
        for digito_2 in nove_digitos + str(digito_1):
            resultado_digito_2 += int(digito_2) * contador_regressivo_2
            contador_regressivo_2 -= 1
        digito_2 = (resultado_digito_2 * 10) % 11
        digito_2 = digito_2 if digito_2 <= 9 else 0

        cpf_gerado_pelo_calculo = f'{nove_digitos}{digito_1}{digito_2}'

        print("Aperte qualquer tecla e 'Enter' para gerar um CPF.")
        input()
        print (f'O Cpf gerado é: {nove_digitos}{digito_1}{digito_2}')