# Crie um programa que leia dois valores e mostre um menu na tela: 
# [1] somar
# [2] multiplicar
# [3] maior
# [4] novos números
# [5] sair do programa
# Seu programa deverá realizar a operação solicitada em cada caso


n1 = int(input('Digite o primeiro valor: '))
n2 = int(input('Digite o primeiro valor: '))
while n1 != 0 and n2 !=0:
    escolha = int(input("""
                        -----MENU-----
                        [1] somar 
                        [2] multiplicar 
                        [3] maior 
                        [4] novos números 
                        [5] sair do programa
                        """))
    if escolha == 1:
        soma = n1 + n2
        print(f'A soma do número {n1} e {n2} é {soma}')
    elif escolha == 2:
        multiplica = n1 + n2
        print(f'A multiplicação do número {n1} e {n2} é {multiplica}')
    elif escolha == 3:
        if n1 > n2:
            print(f'O número {n1} é maior que {n2}')
        else:
            print(f'O número {n2} é maior que {n1}')
    elif escolha == 4:
        n1 = int(input('Digite o primeiro valor: '))
        n2 = int(input('Digite o primeiro valor: '))
    else:
        print('Você saiu!')
        break
    