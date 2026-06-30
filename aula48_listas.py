"""
Listas em Python
Tipo list - Mutável
Suporta vários valores de qualquer tipo
Conhecimentos reutilizaveis - indices e fatiamentos
Métodos úteis: append, insert, pop, del, clear, extend, +
"""

#       01234
#      -54321
string = 'ABCDE'  # 5 caracteres (len)
# print(bool(lista))
# print(lista, type(lista))

#         0     1           2       3     4
#        -5    -4          -3      -2    -1  
lista = [123, True, 'Gabriel Melo', 1.2, []]
lista[2] = 'Márcia'
print(lista[2], type(lista[2]))
print(lista)