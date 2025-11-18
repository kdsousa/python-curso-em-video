# Faça um programa que joque par ou impar com o computador. O jogo só será interrompido quando o jogador PERDER,
# mostrando o total de vitórias consecutivas que ele conquistou no final do jogo.
from random import randint

v = 0

while True:
    jogador = int(input('Diga um valor: '))
    computador = randint(0, 11)
    total = jogador + computador
    tipo = ' '

    while tipo not in 'PI':
        tipo = str(input('Par ou Ímpar? [P/I]')).strip().upper()[0]

    print(f'Você jogou {jogador} e o computador  {computador}. Total de {total}')

    if tipo == 'P':
        if total % 2 == 0:
            print('Você venceu')
            v += 1
        else:
            print('Você perdeu')
            break
    elif tipo == 'I':
        if total % 2 == 1:
            print('Você venceu')
            v += 1
        else:
            print('Você perdeu')
            break
        
    print('Vamos jogar novamente')
print(f'Você venceu {v} vezes.')
