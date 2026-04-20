dia = input ("Qual o dia do seu aniversário?: ")
dia_int = int(dia)
mes = input ("Que mês você nasceu?: ")
ano_nascimento = input ("Que ano você nasceu?: ")
ano_nascimento_int = 2026 - int(ano_nascimento)
ano_bissexto = (-(ano_nascimento_int // -4))
dias_ano_atual = 31 + 28 + 31 + 14

print (ano_nascimento_int * (365) + ano_bissexto + dias_ano_atual - dia_int)
