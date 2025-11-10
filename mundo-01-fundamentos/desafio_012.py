"""
Faça um algoritimo que leia o preço de um produto e mostre seu novo preço, com 5% de desconto
"""
p = float(input('Digite o valor do protudo: '))
desconto = p * 0.05
np = p - desconto
print(f"Preço original: R${p:.2f}")
print(f"Desconto de 5%: R${desconto:.2f}")
print(f"Novo preço: R${np:.2f}")
