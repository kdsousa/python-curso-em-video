# Faça um programa que leia uma frase pelo teclado e mostre:
# Quantas vezes aparece a letra "A".
# em que posição ela aparece a primeira vez
# em que posição ela aparece a última vez.
frase = str(input('Digite uma frase: ')).strip().upper()
print(f'Na frase que digitou temos {frase.count('A')} lestras "A"')
print(f'A primeira letra "A" aparece na posição {frase.find('A') + 1}')
print(f'A Ultima letra "A" aparece na posição {frase.rfind('A') + 1}')
