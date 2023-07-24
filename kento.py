num = input('Digite um número inteiro e direi se ele é ímpar ou par: ')

if num.isdigit():
    num = int(num)
    if num % 2 == 0: print('Este número é par.')
    else: print('Este número é ímpar.')
else:
    print('Digite um número inteiro válido.')