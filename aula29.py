lista_de_compras = []

while True:
    opcoes = input('[i]nserir [a]pagar [l]istar: ')
    letras_permitidas = 'i' 'a' 'l'
    if opcoes not in letras_permitidas:
        print('não valido')
        continue
    elif opcoes == 'i':
        lista = input('Qual é o item que deseja adicionar: ')
        lista_de_compras.append(lista)
    elif opcoes == 'a':
        if lista_de_compras == []:
            print('Sua lista está vazia')
            continue
        excluir = input('Qual item você deseja excluir: ')
        apagar = int(excluir)
        lista_de_compras.pop(apagar)
    elif opcoes == 'l':
        if lista_de_compras == []:
            print('Sua lista está vazia')
            continue
        for indice, nome in enumerate(lista_de_compras):
            print(f'A sua lista e indices dela é: {indice, nome}')
    continue
