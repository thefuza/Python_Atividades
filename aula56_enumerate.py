"""
enumerate - enumra itevraveis (indices)
"""
lista = ['Maria', 'Helena', 'Luiz']
lista.append('João')

# lista_enumerada = list(enumerate(lista))


# print(lista_enumerada)

for indice, nome in enumerate(lista):
    print(indice, nome)

# for item in enumerate(lista):
#     indice, nome = item
#     print(indice, nome)

# for tupla_enumerada in enumerate(lista):
#     print('FOR DA TUPLA: ')
#     for valor in tupla_enumerada:
#         print(f'\t{valor}')
        

