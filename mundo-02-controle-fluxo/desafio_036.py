# Escreva um programa para aprovar o empréstimo bancário para a compra de uma casa.
# O programa vai perguntar o valor da casa, o salário do comprardor e em quantos anos ele vai pagar
# Calcule o valor da prestação mensal, sabendo que ela não pode exceder 30% do salário ou então o empréstimo será negado

v_casa = float(input('Digite o valor da casa R$'))
s = float(input('Digite o valor do salario R$'))
ano = int(input('Digite em quantos anos quer pagar: '))
meses = ano * 12
v_prestacao = s * 0.30
prestacao_casa = v_casa / meses

if prestacao_casa > v_prestacao:
    print(f'Para pagar uma casa de R${v_casa} em {ano} anos a prestação será de R${prestacao_casa}')
    print('Emprestimo negado')
else:
    print(f'Para pagar uma casa de R${v_casa} em {ano} anos a prestação será de R${prestacao_casa}')
    print('Emprestimo aprovado')
    