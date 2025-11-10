# Faça um programa que leia um número de 0 a 9999 e mostre na tela cada um dos dígitos separados.
# Ex: Digite um número: 1834
# Unidade: 4
# Dezena: 3
# Centena: 8
# Milhas: 1
n = int(input('Digite um valor de 0 a 9999: '))
u = n // 1 % 10
d = n // 10 % 10
c = n // 100 % 10
m = n // 1000 % 10

print(f'O número {n} tem {u} unidade')
print(f'O número {n} tem {d} dezena')
print(f'O número {n} tem {c} centena')
print(f'O número {n} tem {m} milhar')
