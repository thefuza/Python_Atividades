"""
Listas em Python
Tipo list - Mutável
Suporta vários valores de qualquer tipo
Conhecimentos reutilizaveis - indices e fatiamentos
Métodos úteis: 
    append - Adiciona um item ao final
    insert - Adiciona um item no indice escolhido
    pop - Remove do final ou do indice escolhido
    del - apaga um indice
    clear - limpa a lista
    extend - estende a lista
    + - concatena listas
Create, Read, Update, Delete
Criar,  ler,  alterar, apagar = lista[i] CRUD

"""
lista = [10, 20, 30, 40]
lista.append('Gabriel')
nome = lista.pop()
lista.append(1233)
del lista[-1]
# lista.clear()
lista.insert(100, 5)
print(lista[4])   