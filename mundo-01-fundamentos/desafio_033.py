# Faça um programa que leia três números e mostre qual é o maior e qual é o menor.
n1 = int(input('Digite o primeiro núemro: '))
n2 = int(input('Digite o segundo núemro: '))
n3 = int(input('Digite o terceiro núemro: '))

if n1 > n2 and n1 > n3:
    print(f' O número maior é {n1}')
elif n2 > n1 and n2 > n3:
    print(f' O número maior é {n2}')
else:
    print(f' O número maior é {n3}')
    