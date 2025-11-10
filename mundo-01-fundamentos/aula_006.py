n1 = int(input('Digite um valor: ')) # recebe números
n2 = int(input('Digite outro valor: '))
s = n1 + n2
print(type(n1)) # mostra o tipo de dados
print(f'A soma é: {s}')

n = input('Digite algo: ')
print(n.isnumeric()) # se é numero
print(n.isalpha()) # se é letra
print(n.isalnum()) # se é alfanumerico
print(n.isupper()) # ver se esta tudo em maiuscula
