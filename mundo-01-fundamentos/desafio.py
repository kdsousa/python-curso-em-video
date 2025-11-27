''' Crie um script Python que leia o dia, o mês e o ano de nascimento de uma pessoa e mostre uma mensagem com a data formatada.'''
dia = input('Digite o dia do seu nascimento: ')
mes = input('Digite o mês de seu nascimento: ')
ano = input('Digite o ano de nasciemnto: ')

print(dia, end='/')
print(mes, end='/')
print(ano)
print(f'Você nasceu no dia {dia} do mês {mes} de {ano}')
