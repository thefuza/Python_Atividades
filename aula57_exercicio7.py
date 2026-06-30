"""
Faça uma lista de compras com linhas
O usuário deve ter a possibilidade de
inserir, apagar e listar valores da sua lista
Não permita que o programa quebre com
erros de indices inexistentes na lista
"""

# lista_de_compras = ['Arroz', 'Feijão', 'Macarrão']

# for lista in enumerate(lista_de_compras):
#     print(lista)

opcao = ''
lista = []
item = ''
indice = ''

while True:
    opcao = input('======================================\n' \
            '\tSelecione uma opção: \n' \
            '======================================\n'\
    '[i]nserir\n' \
    '[a]pagar\n' \
    '[l]istar\n' \
    '[s]air\n' \
    'Digite a opção: ')

    if opcao == 'i':
        print('=============================================\n' \
        '\tInsira um item a sua lista\n' \
        '=============================================')
        item = (input('Digite o item que deseja adicionar: '))
        
        if item in lista:
            print('Já existe um item com esse nome')
            continue
        else:
            lista.append(item)
            continue
                
                

    if opcao == 'a':
        print('=============================================\n' \
                '\tRemova um item da lista\n' \
                '=============================================')
        if not lista:
            print('Tenha pelo menos um item na sua lista de compras')
        else:
            
            for indice, nome in enumerate(lista):
                print(indice, nome)

            indice = int(input("Digite o numero do item que desejar remover: "))
            if 0 <= indice < len(lista):
                del lista[indice]
            else:
                print('Não existe este item na lista!')


    if opcao == 'l':
        if not lista:
            print('Não há itens na lista de compras!')
        else:
            print(f'=============================================\n' \
                    '\tTotal de itens da sua lista de compras \n'
                    '=============================================')
            for indice, nome, in enumerate(lista):
                print(indice, nome)
            continue
              
    if opcao == 's':
        print('=============================================\n' \
        '\tVocê saiu da lista de compras!\n' \
        '=============================================')
              
        break


