# Faça um programa que leia o sexo de uma pessoa, mas só aceite os valores 'M' ou 'F'.
# Caso esteja errado, peça a digitação novamente até ter um valor correto.
sexo = ''

while sexo != 'F' and sexo != 'M':
    sexo = str(input('Digite o sexo [F/M]: ')).strip().upper()

    if sexo != 'F' and sexo != 'M':
        print('Valor inválido. Por favor, digite apenas "F" para Feminino ou "M" para Masculino.')

print(f'\nO sexo que você digitou foi: {sexo}')
