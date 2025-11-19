#  Desenvolva um programa que leia quatro valores pelo teclado e guarde-o em uma tupla. No final, mostre:
# A) Quantas vezes apareceu o valor 9
# B) Em que posição foi digitado o primeiro valor 3 
# C) Quais foram os números pares

num = (int(input(input('Digite um número: )'))),
       int(input(input('Digite um número: )'))),
       int(input(input('Digite um número: )'))),
       int(input(input('Digite um número: )'))))

print(f'Você digitou os valores {num}')
print(f'O valor 9 apareceu {num.count(9)} vezes')
if 3 in num:
    print(f'O valor 3 aspareceu na {num.index(3)+1} posição')
else:
    print(f'O valor 3 nãp foi digitado em nenhuma posição')
print('Os valores pares digitados foram')
for n in num:
    if n % 2 ==0:
        print(n)
