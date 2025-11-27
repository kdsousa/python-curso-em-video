# Desenvolva um programa que pergunte a distância de uma viagem em Km. 
# Calcule o preço da passagem, cobrando R$0,50 por Km para viagens de até 200Km
# e R$0,45 para viagens mais longas
d = int(input('Digite a distancia em Km: '))

if d <= 200:
    v = d * 0.50
    print(f' O valor da viagem de {d}km é de R${v:.2f}')
else:
    v = d * 0.45
    print(f' O valor da viagem de {d}km é de R${v:.2f}')
    