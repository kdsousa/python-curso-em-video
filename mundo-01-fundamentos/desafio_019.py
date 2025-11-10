# Um professor quer sortear  um dos seus quatro alunos 
# para apagar o quadro. faça um programa que ajuda ele, lendo o nome deles e escrevendo o nome do escolhido
import random
aluno1 = input('Primeiro aluno: ')
aluno2 = input('Segundo aluno: ')
aluno3 = input('Terceiro aluno: ')
aluno4 = input('Quarto aluno: ')

lista_alunos = [aluno1, aluno2, aluno3, aluno4]
aluno_sorteado = random.choice(lista_alunos)
print(f' O aluno escolhido para apagar o quadro foi: {aluno_sorteado}')
