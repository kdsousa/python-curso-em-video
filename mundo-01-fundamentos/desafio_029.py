# Escreva um programa que leia a velocidade de um carro.
# Se ele ultrapassar 80Km/h, mostre uma mensagem dizendo que ele foi multado.
# A multa vai custar R$7,00 por cada Km acima do limite.

v = int(input('Digite a sua velocidade: '))
multa = 0
while v > 80:
    print('Você foi multado!')
    multa = (v - 80) * 7
    print(f'Valor da multa R${multa}')
    v = int(input('Digite a sua velocidade: '))
