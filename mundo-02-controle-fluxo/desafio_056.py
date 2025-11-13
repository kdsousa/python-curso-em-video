# Desenvolva um programa que leia o nome, idade e sexo de 4 pessoas. No final do programa, mostre:
# A média de idade do grupo.
# Qual é o nome do homem mais velho.
# Quantas mulheres tèm menos de 20 anos.
somaidade = 0
mediaidade = 0
maioridadehomem = 0
nomevelhor = ''
totmulher20 = 0

for p in range(1, 5):
    print(f'--------- {p} Pessoa ---------')
    nome = str(input('Nome: ')).strinp()
    idade = int(input('Idade: '))
    sexo = str(input('Sexo [M/F]: '))
    somaidade += idade
    if p == 1 and sexo in 'Mm':
        maioridadehomem = idade
        nomevelhor = nome
    if sexo in 'Mm' and idade > maioridadehomem:
        maioridadehomem = idade
        nomevelhor = nome
    if sexo in 'Ff' and idade < 20:
        totmulher20 += 1
mediaidade = somaidade / 4
print(f'A média de idade do grupo é de {mediaidade} anos')
print(f'O homem mais velhor tem {maioridadehomem} anos e se chama {nomevelhor}')
print(f'Ao todo são {totmulher20} mulheres com menos de 20 anos')
