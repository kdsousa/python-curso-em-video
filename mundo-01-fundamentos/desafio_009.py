# Faça um programa que leia um número Inteiro qualquer e mostre na tela a sua tabuada
n = int(input('Digite o numero da tabuada que deseja ver: '))
contador = 0
for ncontador in range(11):
    print(f'{n} * {contador} = {n * contador}')
    contador = contador + 1
