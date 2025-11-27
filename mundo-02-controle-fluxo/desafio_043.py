# Desenvolva uma lógica que leia o peso e a altura de uma pessoa, calcule seu IMC e mostre seu status, de acordo com a tabela abaixo:
# - Abaixo de 18.5: Abaixo do Peso
# - Entre 18.5 e 25: Peso ideal
# - 25 até 30: Sobrepeso
# - 30 até 40: Obesidade
# - Acima de 40: Obesidade móirbida
peso = float(input('Qual é seu peso? '))
altura = float(input('Qual é a sua altura? '))
imc = peso / (altura ** 2)

print(f'O IMC dessa pessoa é de {imc:.1f}')
if imc < 18.5:
    print('Você está abaixo do peso normal')
elif imc < 25:
    print('Você está no peso normal')
elif imc < 30:
    print('Você está com sobrepeso')
elif imc < 40:
    print('Você está com Obesidade')
else:
    print('Você está com Obesidade Mórbida')
