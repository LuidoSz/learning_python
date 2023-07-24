nome = input('digita seu nome plebeu: ')
tamanho_nome = len(nome.replace(" ",""))




if tamanho_nome > 1:
    if tamanho_nome <= 4:
        print('Seu nome é curto')
    elif tamanho_nome >= 5 and tamanho_nome <= 6:
        print('Seu nome é normal')
    else:
        print('seu nome é longo')
else: 
    print('Digita mais')