import sys
import re

cpf_enviado_pelo_usuario = input('Digite seu CPF: ')\
#     .replace('.', '') \
#     .replace(' ', '') \
#     .replace('-', '')
cpf_enviado_pelo_usuario = re.sub(
    r'[^0-9]',
    '',
    cpf_enviado_pelo_usuario
)

cpf_e_sequencial = cpf_enviado_pelo_usuario == cpf_enviado_pelo_usuario * len(cpf_enviado_pelo_usuario)

if cpf_e_sequencial :
    print('CPF inválido.')
    sys.exit()    

# string
# 

nove_digitos = cpf_enviado_pelo_usuario[:9]
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

if cpf_enviado_pelo_usuario == cpf_gerado_pelo_calculo:
    print(f'{cpf_enviado_pelo_usuario} é válido.')
else:
    print("Cpf inválido.")
