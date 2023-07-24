nome = input('Digita seu nome: ')
idade = input('Digita sua idade: ')
if nome and idade:
    print(f'Seu nome é {nome}')
    print(f'Seu nome invertido é {nome[::-1]}')
    print(f'Seu nome tem', len(nome.replace(" ", "")))
    if ' ' in nome:
        print('Seu nome possui espaço')
    else: 
        print('não possui espaços')
    print(f'Primeira letra do seu nome é {nome[0]}')
    print(f'ultima letra do seu nome é {nome[-1]}')