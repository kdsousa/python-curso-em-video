# Melhore o jogo do DESAFIO 028 onde o computador vai 'pensar' em um número entre 0 e 10. Só que agora o jogador vai 
# tentar adivinhar até acertar, mostrando no final quantos palpites foram necessprarios para vencer
import random

contador = 0
num_aleatorio = str(random.randint(0, 10))
escolha = ''

while escolha != num_aleatorio:
    contador += 1
    print(f'tentativa {contador}')
    escolha = str(input('Digite o número entre 0 a 10: '))
    print('Voce errou')

print(f'você acerou o número secreto {num_aleatorio} em {contador} chances')
    