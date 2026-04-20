dia = input ("Digite o dia de seu nascimento: ")
dia_int = int(dia)
mes = input("Digite seu mês de nascimento (número ou nome): ").strip()
meses_dict = {
    "janeiro": 1, "fevereiro": 2, "março": 3, "abril": 4, "maio": 5, "junho": 6,
    "julho": 7, "agosto": 8, "setembro": 9, "outubro": 10, "novembro": 11, "dezembro": 12
}
try:
    if mes.isdigit():
        mes_int = int(mes)
    else:
        mes_int = meses_dict[mes.lower().strip()]
except (ValueError, KeyError):
    print("Mês inválido. Por favor, insira o número ou nome do mês corretamente.")
    quit()
ano_nascimento = input('Digite seu ano de nascimento: ')
try:
    ano_nascimento_int = int(ano_nascimento)

    if ano_nascimento_int < 1900 or ano_nascimento_int > 2026:
        print("Ano de nascimento inválido. Por favor, insira um ano entre 1900 e 2026.")
        quit()
except ValueError:
    print("Valor inválido. Por favor, insira números inteiros para mês, dia e ano de nascimento.")
    quit()

idade = 2026 - ano_nascimento_int

# Calcula o número de anos bissextos entre o ano de nascimento e 2026 (exclusivo)
leap_years = 0
for year in range(ano_nascimento_int, 2026):
    if (year % 4 == 0 and year % 100 != 0) or (year % 400 == 0):
        leap_years += 1

dias_idade = idade * 365 + leap_years

janeiro_int = 31
fevereiro_int = 28
março_int = 31
abril_int = 30
maio_int = 31
junho_int = 30
julho_int = 31
agosto_int = 31
setembro_int = 30
outubro_int = 31
novembro_int = 30
dezembro_int = 31

mes_normalizado = mes.strip().lower()
if mes_normalizado in ["janeiro", "1"]:
    mes_normalizado = janeiro_int - dia_int
elif mes_normalizado in ["fevereiro", "2"]:
    mes_normalizado = fevereiro_int - dia_int
elif mes_normalizado in ["março", "marco", "3"]:
    mes_normalizado = março_int - dia_int
elif mes_normalizado in ["abril", "4"]:
    mes_normalizado = abril_int - dia_int
elif mes_normalizado in ["maio", "5"]:
    mes_normalizado = maio_int - dia_int
elif mes_normalizado in ["junho", "6"]:
    mes_normalizado = junho_int - dia_int
elif mes_normalizado in ["julho", "7"]:
    mes_normalizado = julho_int - dia_int
elif mes_normalizado in ["agosto", "8"]:
    mes_normalizado = agosto_int - dia_int
elif mes_normalizado in ["setembro", "9"]:
    mes_normalizado = setembro_int - dia_int
elif mes_normalizado in ["outubro", "10"]:
    mes_normalizado = outubro_int - dia_int
elif mes_normalizado in ["novembro", "11"]:
    mes_normalizado = novembro_int - dia_int
elif mes_normalizado in ["dezembro", "12"]:
    mes_normalizado = dezembro_int - dia_int

print (dias_idade )
