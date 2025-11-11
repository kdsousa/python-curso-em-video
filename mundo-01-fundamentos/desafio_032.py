# Faça um programa que leia um ano qualquer e mostre se ele é BISSEXTO
ano = int(input("Digite um ano para saber se é bissexto: "))

if (ano % 4 == 0 and ano % 100 != 0) or (ano % 400 == 0):
    print(f"O ano de {ano} é BISSEXTO.")
else:
    print(f"O ano de {ano} NÃO é bissexto.")
    