# Tuplas 
# As tuplas são IMUTAVEIS
lanche = ('Hambúrguer', 'Suco', 'Pizza', 'Pudim', 'Batata Frita')

print(lanche) # Imprimindo a tupla
print(lanche[1]) # Imprimindo o elemento 1 da tupla

for comida in lanche: # Iterando a tupla
    print(f'Eu vou comer {comida}!')

print('Comi pra caramba!')

for cont in range(0, len(lanche)): # Se precisar da posição
    print(lanche[cont])

for pos, comida in enumerate(lanche): # Se precisar da posição
    print(f'Eu vou comer {comida} na posição {pos}!')

print('Comi pra caramba!')

print(sorted(lanche)) # Mostra a tupla em ordem 
print(lanche)

a = (2, 5, 4)
b = (5, 8, 1, 2)
c = a + b

print(c)
print(len(c)) # Conta os elementos da tupla
print(c.count(5)) # Mostra quantas vezes o 5 aparece na tupla
print(c.index(8)) # Mostra em que posição o 8 está 

pessoa = ('Gustavo', 39, 'M', 99.88)

print(pessoa)

del(pessoa) # Apaga a tupla
