# Condições if, elif e else
tempo = int(input('Quantos anos tem seu carro: '))
# print('carro novo' if tempo <=3 else 'carro velho')
if tempo <= 3:
    print('Carro novo')
else:
    print('Carro velho')

print('---FIM---')

nome = str(input('Qual é seu nome? '))
if nome == 'Keplin':
    print('Que nome lindo você tem!')
else:
    print('Seu nome é tão normal!')
print(f'Bom dia, {nome}!')
