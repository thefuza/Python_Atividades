"""
Iteravel -> str, range, etc (__iter__)
Iterador -> quem sabe entregar um valor por vez
next -> me entregue o próximo
iter -> me entregue seu iterador 
"""
texto = 'Luiz' # iteravel
iterador = iter(texto) # iterator

# while True:
#     try:
#         letra = next(iterador) 
#         print(letra)
#     except StopIteration:
#         break

for letra in texto:
    print(letra)



