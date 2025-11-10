# Faça um programa que leia um ângulo qualquer e mostre na tela o valor do seno, cosseno e tangente desse ângulo.
import math

angulo_graus = float(input('Digite o ângulo (em graus) que você deseja: '))
angulo_radianos = math.radians(angulo_graus)
seno = math.sin(angulo_radianos)
cosseno = math.cos(angulo_radianos)
tangente = math.tan(angulo_radianos)
print(f'Para o ângulo de {angulo_graus}°:')
print(f'O valor do SENO é: {seno:.2f}')
print(f'O valor do COSSENO é: {cosseno:.2f}')
print(f'O valor da TANGENTE é: {tangente:.2f}')
