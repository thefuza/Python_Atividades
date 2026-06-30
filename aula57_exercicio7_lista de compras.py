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

import os


opcao = ''
lista = []
item = ''
indice = ''

while True:
    opcao = input('=============================================\n' \
            '\t  Selecione uma opção: \n' \
            '=============================================\n'\
    '[i]nserir\n' \
    '[a]pagar\n' \
    '[l]istar\n' \
    '[s]air\n' \
    'Digite a opção: ')

    if opcao == 'i':
        os.system('cls')
        print('=============================================\n' \
        '\tInsira um item a sua lista\n' \
        '=============================================')
        item = (input('Digite o item que deseja adicionar: '))
        
        if item in lista:
            os.system('cls')
            print('Já existe um item com esse nome')
            continue
        else:
            os.system('cls')
            lista.append(item)
            print(f'{item}, adicionado à lista de compras!')
            continue

    elif opcao == 'a':
        os.system('cls')
        print('=============================================\n' \
                '\tRemova um item da lista\n' \
                '=============================================')
        if not lista:
            
            print('Tenha pelo menos um item na sua lista de compras')
        else:
            
            for indice, produto in enumerate(lista):
                print(indice, produto)

        
            print('=============================================\n')
            indice_str = input("Digite o numero do item que desejar remover: ")

            try:        
                if 0 <= indice < len(lista):
                    os.system('cls')
                    indice = int(indice_str)
                    del lista[indice]
                    print(f'{item} foi removido da lista de compras')
        
            except IndexError:
                os.system('cls')
                print(f'Digite um valor entre 0 e {len(lista)}')
            
            except ValueError:
                os.system('cls')
                print('Digite um valor válido (inteiro)!')
        

    elif opcao == 'l':
        os.system('cls')
        if not lista:
            print('Não há itens na lista de compras!')
        else:
            print(f'=============================================\n' \
                    '   Total de itens da sua lista de compras \n'
                    '=============================================')
            for indice, produto, in enumerate(lista):
                print(indice, produto)
            continue
              
    elif opcao == 's':
        os.system('cls')
        print('=============================================\n' \
        '\tVocê saiu da lista de compras!\n' \
        '=============================================')
              
        break

    else:
        os.system('cls')
        print('Por favor, escolha umas das opções acima')
