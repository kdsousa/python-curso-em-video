""" Faça um programa que leia algo pelo teclado e mostre na tela o seu tipo primitivo e todas as informações sobre ele."""
algo = input('Digite algo: ')
print(f'O que você digitou é {algo.isnumeric()} para Número')
print(f'O que você digitou é {algo.isalpha()} para Letra')
print(f'O que você digitou é {algo.isalnum()} para Alfanumerico')

