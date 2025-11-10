# Importando modulos 
import math # importando tudo da biblioteca de matemática
from math import sqrt # importando apenas um modulo da biblioteca 'sqrt'
num = int(input('Digite um número: '))
raiz = math.sqrt(num) # Modo com 'import math'
raiz = sqrt(num) # modo com 'from math import sqrt'
print(f'A raiz de {num} pe igual a {raiz:.2f}')

import random # biblioteca para gerar números pseudoaleatórios e realizar operações randômicas
num = random.randint(1, 10) # gera um número inteiro aleatório ente 1 e 10
print(num)

import emoji # biblioteca para usar emojjis
print(emoji.emojize('Olá, mundo :sunglasses:'))
