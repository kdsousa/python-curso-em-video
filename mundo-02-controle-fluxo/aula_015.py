# Interrompendo repetições while
n = s = 0
while True:
    n = int(input('Digite um número: '))
    if n == 99:
        break
    s += n 
print(f'A soma vale {s}')
