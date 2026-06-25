"""
Iterando strings com while
"""
#       01234567891011
nome = 'Stefany Elias de Melo' # Iteraveis
#       121110987654321
# tamanho_nome = len(nome)
# novo_nome = ''
# print(nome)
# print(tamanho_nome)

# print(nome[3])

# indice = 0

# while indice < len(nome):
    
#     novo_nome = novo_nome +'*'+ nome[indice]
#     indice += 1

# print(novo_nome)

# Versão de resposta do professor

tamanho_nome = len(nome)
novo_nome = ''
print(nome)
print(tamanho_nome)

print(nome[3])

indice = 0

while indice < len(nome):
    letra = nome[indice]
    novo_nome += f'*{letra}'
    indice += 1

novo_nome += '*'
print(novo_nome)
