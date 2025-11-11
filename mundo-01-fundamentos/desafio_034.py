# Escreva um programa que pergunte o salário de um funcionário e calcule o valor do seu aumento.
# Para salários superiores a R$ 1.250,00, calcule um aumento de 10%
# Para os inferiores ou iguais, o aumento é de 15%

s = float(input('Digite o valor do salário R$'))
if s >= 1250.00:
    s = s + (s * 0.10)
    print(f' Seu novo salário é R${s}')
else:
    s = s + (s * 0.15)
    print(f' Seu novo salário é R${s}')
    