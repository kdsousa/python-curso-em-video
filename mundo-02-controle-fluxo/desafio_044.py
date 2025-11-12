# Elabore um programa que calcule o valor a ser pago por um produto
# considerando o seu preço normal e condição de pagamento:
# - à vista dinheiro/cheque: 10% de desconto
# - à vista cartão: 5% de desconto
# - em até 2x no cartão: preço normal
# 3x ou mais no cartão: 20% de juros

v_produto = float(input('Digite o valor do produto R$'))

print('1 - Pagemento à vista dinheiro/cheque')
print('2 - Pagamento à vista cartão')
print('3 - Pagamento em até 2x no cartão: preço normal')
print('4 - Pagamento em 3x ou mais no cartão')

f_pagamento = int(input('Digite qual das formas de pagamento vai ser: '))

if f_pagamento == 1 :
    v_produto = v_produto - (v_produto * 0.10) 
    print(f'O valor vai ser de R${v_produto}')
elif f_pagamento == 2 :
    v_produto = v_produto - (v_produto * 0.05) 
    print(f'O valor vai ser de R${v_produto}')
elif f_pagamento == 3 :
    print(f'O valor vai ser de R${v_produto}')
else: 
    v_produto = (v_produto * 0.20) + v_produto
    print(f'O valor vai ser de R${v_produto}')
    