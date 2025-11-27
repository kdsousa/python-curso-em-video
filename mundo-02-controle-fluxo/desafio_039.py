# Faça um programa que leia o ano de nascimento de um jovem e informe, de acordo com sua idade:
# - Se ele ainda vai se alistar ao serviço militar.
# - Se é a hora de se alistar.
# - Se já passou do tempo do alistamento
# Seu programa também deverá mostrar o tempo que falta ou que passou do prazo.
ano_nascimento = int(input('Digite o ano de nascimento: '))
ano_atual = 2025
idade = ano_atual - ano_nascimento

if idade < 18:
    print(f'Ainda falta {18 - idade} anos para se alistar ao serviço militar.')
elif idade == 18:
    print('Esta no ano de se alistar ao serviço militar.')
else:
    print(f'Você ja passou do tempo de alistamento em {idade - 18} anos')
