frase = 'Curso em Video Python'
print(frase)

# Fatiamaento [inicio:fim:passo]
print(frase[9]) # Pega o caractere na posição de índice 9
print(frase[9:13]) # Pega os caracteres do índice 9 (incluíndo) até o 13 (excluíndo)
print(frase[9:21]) # Pega os caracteres do índice 9 até o final 
print(frase[9:21:2]) # Pega  do índice 9 até o 21, pulando de 2 em 2 caracteres
print(frase[:5]) # Pega os caracteres do início (índice 0) até o índice5 (excluído)
print(frase[15:]) # Pega os caracteres do índice 15 (incluído) até o final da string
print(frase[9::3]) # Pega do índice 9 até o final, pulando de 3 em 3 caracteres

# Analise
print(len(frase)) # Retorna o comprimento da string
print(frase.count('o')) # Conta quantas vezes a letra 'o' na string
print(frase.count('o', 0, 13)) # Conta quantas vezes a letr 'o' aparece no fatiamento do índice 0 até o 13
print(frase.find('deo')) # Mostra o índice onde o primeiro  'd' da substring 'deo' foi encontrado
print(frase.find('Android')) # Retorna -1 porque a substring 'Android' não foi encontrada na string
print('curso' in frase) # Verifica se a string 'curso' está contida na frase

# Tranformação
print(frase.replace('Python', 'Android')) # Substitui 'Python' por 'Android'
print(frase.upper()) # Retorna a string com todas as letras maiúsculas
print(frase.lower()) # Retorna a string com todas as letras minúsculas
print(frase.capitalize()) # Retorna a string com apenas a primeira letra em maiúscula
print(frase.title()) # Retorna a string com a primeira letra de cada palavra em maiúscula
print(frase.strip()) # Remove espaços em brnacos no início e no fim
print(frase.rstrip()) # Remove espaços em banco do fim 
print(frase.lstrip()) # Remove espaços em banco do início 

# Divisão
print(frase.split()) # Divide a string em uma lista de palavras, usando espaços como separador

# Junção
print('-'.join(frase)) # Junta os caracteres da string, inserindo o separador '-'
