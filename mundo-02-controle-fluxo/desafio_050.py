# Desemvolva um programa que leia seis números inteiros e mostre a soma apenas daqueles
# que forem pares. Se o valor digitado for ímpar, desconsidere-o
lista_1 = ['primeiro', 'segundo', 'terceiro', 'quarto', 'quinto', 'sexto']
contador_1 = 0
lista_2 = []

for c in range (6):
    n = int(input(f'Digite o {lista_1[0]} número: '))
    contador_1 = contador_1 + 1
    lista_2.append(n)
    
contador_2 = 0

for n in lista_2:
    if n % 2 == 0:
        contador_2 = contador_2 + n 
        
print(contador_2)
