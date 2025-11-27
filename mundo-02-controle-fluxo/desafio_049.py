# Refaça o desafio 009, mostrando a tabuada de um número que o usuário escolher, só que agora utilizando um laço for 
n = int(input('Digite o numero da tabuada que deseja ver: '))
contador = 0

for ncontador in range(11):
    print(f'{n} * {contador} = {n * contador}')
    contador = contador + 1
    