"""
for in com listas
"""
lista = ['Maria', 'Helena', 'Luiz']
lista.append('João')
indices = range(len(lista))

print(indices)

for indice in indices:
    print(indice, lista[indice], type(lista[indice]))

# for letra in 'ABC':
#     print(letra)

# for indice, nome in enumerate(lista):
#     print(f'O índice de {nome} é {indice}')

