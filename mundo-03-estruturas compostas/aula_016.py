# Tuplas 
# As tuplas são IMUTAVEIS

lanche = ('Hambúrguer', 'Suco', 'Pizza', 'Pudim', 'Batata Frita')
print(lanche)
print(lanche[1])

for comida in lanche:
    print(f'Eu vou comer {comida}!')
print('Comi pra caramba!')

for cont in range(0, len(lanche)):# se precisar sa posição
    print(lanche[cont])

for pos, comida in enumerate(lanche): # se precisar sa posição
    print(f'Eu vou comer {comida} na posição {pos}!')
print('Comi pra caramba!')

print(sorted(lanche)) # mostra a tupla em ordem 
print(lanche)

a = (2, 5, 4)
b = (5, 8, 1, 2)
c = a + b
print(c)
print(len(c)) # Conta os elementos da tupla
print(c.count(5)) # mostra quantas vezes o 5 aparece na tupla
print(c.index(8)) # mostra em que posição o 8 está 

pessoa = ('Gustavo', 39, 'M', 99.88)
print(pessoa)

del(pessoa) # apaga a tupla