# Escreva um programa que leia um número inteiro qualquer e peça para o usuário escolher qual será a base de conversão:
# 1 para binário
# 2 para octal
# 3 para hexadecimal
n = int(input('Digite o um número para conversão: '))

print('1 - para converter para Binário')
print('2 - para converter para Octal')
print('3 - para converter para Hexadecimal')

opcao = int(input('Digite o número da opção: '))

if opcao == 1:
    print(f'{n} convertido ára Binário é igual a {bin(n)[2:]}')
elif opcao == 2:
    print(f'{n} convertido ára Octal é igual a {oct(n)[2:]}')
elif opcao == 3:
    print(f'{n} convertido ára Hexadecimal é igual a {hex(n)[2:]}')
else:
    print('Opção invalida')
