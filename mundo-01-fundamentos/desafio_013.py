# Faça um algoritimo que leia o salário de um funcionario e mostre seu novo salário, com 15% de aumento.
s = float(input('Digite o seu dalario para o calculo: '))
a = s * 0.15
ns = s + a
print(f' Seu sal´srio é R${s}')
print(f'O aumento de 15% é de R${a}')
print(f'O seu novo salário é de R${ns}')