# Refaça o desafio 035 dos triângulos, acrescentando o recurso de mostrar que tipo de triângulo será formado:
# - Equilátero: Todos os lados iguais
# - Isósceles: Dois lados iguais
# - Escaleno: todos os lados diferentes
r1 = float(input('Digite o primeiro segmento: '))
r2 = float(input('Digite o segundo segmento: '))
r3 = float(input('Digite o terceiro segmento: '))

if r1 < r2 + r3 and r2 < r1 + r3 and r3 < r1 + r2:
    print(' Os seguimentos podem formar um triangulo')
    if r1 == r2 and r2 == r3:
        print('é um Triângulo Equilátero')
    elif r1 == r2 or r1 == r3 or r2 == r3:
        print('é um Triângulo Isóceles')
    else:
        print('é um Triângulo Escaleno')
else:
    print(' Os seguimentos não podem formar um triangulo')
