# Crie um programa que faça o computador jogar jokenpô com você
import random

print('Vamos jogar Jokenpô!')
print('O nosso Jokenpô tem as Seguintes opções:')
print('PAPEL')
print('PEDRA')
print('TESOURA')

escolha = str(input('Digite sua escolha: ')).upper().strip()
opcoes = ['TESOURA', 'PEDRA', 'PAPEL']
escolha_maquina = random.choice(opcoes)

print('JO')
print('KEN')
print('PO!!')

if escolha == 'TESOURA' and escolha_maquina == 'PEDRA':
    print(f'Você jogou {escolha} e a máquina jogou {escolha_maquina}')
    print('PERDEU!')
elif escolha == 'TESOURA' and escolha_maquina == 'PAPEL':
    print(f'Você jogou {escolha} e a máquina jogou {escolha_maquina}')
    print('GANHOU!')
elif escolha == 'TESOURA' and escolha_maquina == 'TESOURA':
    print(f'Você jogou {escolha} e a máquina jogou {escolha_maquina}')
    print('EMPATE')
elif escolha == 'PEDRA' and escolha_maquina == 'PEDRA':
    print(f'Você jogou {escolha} e a máquina jogou {escolha_maquina}')
    print('EMPATE')
elif escolha == 'PEDRA' and escolha_maquina == 'PAPEL':
    print(f'Você jogou {escolha} e a máquina jogou {escolha_maquina}')
    print('PERDEU')
elif escolha == 'PEDRA' and escolha_maquina == 'TESOURA':
    print(f'Você jogou {escolha} e a máquina jogou {escolha_maquina}')
    print('GANHOU')
elif escolha == 'PAPEL' and escolha_maquina == 'PEDRA':
    print(f'Você jogou {escolha} e a máquina jogou {escolha_maquina}')
    print('GANHOU')
elif escolha == 'PAPEL' and escolha_maquina == 'PAPEL':
    print(f'Você jogou {escolha} e a máquina jogou {escolha_maquina}')
    print('EMPATE')
elif escolha == 'PAPEL' and escolha_maquina == 'TESOURA':
    print(f'Você jogou {escolha} e a máquina jogou {escolha_maquina}')
    print('PERDEU')
