# Crie um programa que leia quanto dinheiro uma pessoa tem na carteira e mostre quantos Dólares ela pode comprar.
# Considere US$ 1.00 = R$3,27
v = float(input('Digite o valor que tem na carteira para comprar dolares: '))
d = 3.27
conversao = v // d
print(f'Você pode comprar ${conversao} Dolares com o valor de R$ {v}')