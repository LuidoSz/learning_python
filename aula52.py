import random

while True:
    condicao = input('Deseja gerar um novo CPF? [s]im ou [n]ão: ').lower()
    if condicao == 's':

        nove_digitos = ''.join(str(random.randint(0, 9)) for _ in range(9))
        print(f'Os nove dígitos do seu cpf são {nove_digitos}')
        soma1 = sum(int(digito) * (10 - indice) for indice, digito in enumerate(nove_digitos))
        digito1 = 0 if soma1 % 11 < 2 else 11 - soma1 % 11

        print(f'O seu primeiro dígito é {digito1}')

        dez_digitos = nove_digitos + str(digito1)
        soma2 = sum(int(digito) * (11 - indice) for indice, digito in enumerate(dez_digitos))
        digito2 = 0 if soma2 % 11 < 2 else 11 - soma2 % 11

        print(f'O segundo dígito é {digito2}')
        cpf_final = f'{nove_digitos}{digito1}{digito2}'
        print(f'O seu novo CPF é {cpf_final}')

    elif condicao == 'n':
        print('Ok. Saindo do sistema')
        exit()
    else:
        print('Por favor, digite uma das opções válidas')