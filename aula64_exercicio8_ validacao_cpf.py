"""
CALCULO DO PRIMEIRO DIGITO DO CPF
CPF: 746.824.890-70
Colete a soma dos 9 primeiros digitos do CPF
multiplicando cada um dos valores por uma
contagem regressiva começando de 10

Ex.:  746.824.890-70 (746824890)
   10  9  8  7  6  5  4  3  2
*  7   4  6  8  2  4  8  9  0
   70  36 48 56 12 20 32 27 0

Somar todos os resultados:
70+36+48+56+12+20+32+27+0 = 301
Multiplicar o resultado anterior por 10
301 * 10 = 3010
Obter  o resto da divisão da conta anterior por 11
3010 % 11 = 7
Se o resultado anterior foi maior que 9
    resultado é 0
contrario disso:
    resultado é o valor da conta

O primeiro digito do CPF é 7



CALCULO DO SEGUNDO DIGITO DO CPF
CPF: 746.824.890-70
Colete a soma dos 9 primeiros digitos do CPF,
MAIS PRIMEIRO DIGITO,
multiplicando cada um dos valores por uma
contagem regressiva começando de 11

Ex.:  746.824.890-70 (746824890)
   11  10 9  8  7  6  5  4  3  2
*  7   4  6  8  2  4  8  9  0  7  <-- PRIMEIRO DIGITO
   77  40 54 64 14 36 40 26 0 14

Somar todos os resultados:
77+40+54+64+14+36+40+26+0+14 = 363
Multiplicar o resultado anterior por 10
363 * 10 = 3630
Obter  o resto da divisão da conta anterior por 11
3630 % 11 = 0
Se o resultado anterior foi maior que 9
    resultado é 0
contrario disso:
    resultado é o valor da conta

O primeiro digito do CPF é 7

"""

# import re
# import sys


# # cpf_enviado_pelo_usuario = '746.824.890-70'.replace('.', '').replace('-','').replace(' ','')
# entrada = input('CPF [746.824.890-70]: ')
# cpf_enviado_pelo_usuario = re.sub(
#     r'[^0-9]',
#     '',
#     '746.824.890-70')

# entrada_e_sequencial = entrada == entrada[0] * len(entrada)

# if entrada_e_sequencial:
#     print('Você enviou dados sequenciais.')
#     sys.exit()


import random
import sys

for _ in range(100):
    nove_digitos = ''
    for i in range(9):
        nove_digitos += str(random.randint(0, 9))


    contador_regressivo_1 = 10

    resultado_digito_1 = 0
    for digito in nove_digitos:
        resultado_digito_1 += int(digito) * contador_regressivo_1
        contador_regressivo_1 -= 1
    digito_1 = (resultado_digito_1 * 10) % 11
    digito_1 = digito_1 if digito_1 <= 9 else 0


    dez_digitos = nove_digitos + str(digito_1)
    contador_regressivo_2 = 11

    resultado_digito_2 = 0
    for digito in dez_digitos:
        resultado_digito_2 += int(digito) * contador_regressivo_2
        contador_regressivo_2 -= 1
    digito_2 = (resultado_digito_2 * 10) % 11
    digito_2 = digito_2 if digito_2 <= 9 else 0

    cpf_gerado_pelo_calculo = f'{nove_digitos}{digito_1}{digito_2}'

    print(cpf_gerado_pelo_calculo)
