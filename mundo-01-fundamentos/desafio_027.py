# Faça um programa que leia o nome completo de uma pessoa, mostrando em seguida o primeiro e o último nome separamente.
# Ex: Ana Maria de Souza
# primeiro = Ana
# último = Souza
nome = str(input('Digite um nome: ')).strip().title()
lista = nome.split()

print(lista)
print(f'O primeiro nome é {lista[0]}')
print(f'O último nome é {lista[-1]}')
