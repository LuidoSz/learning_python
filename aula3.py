nome = input('Qual é seu nome? ')
numero_1 = input('Digite um número: ')
numero_2 = input('Digite outro número: ')

if numero_1 == int:
    numero_1 = int(numero_1)
else:
    numero_1 = float(numero_1)
if numero_2 == int:
    numero_2 = int(numero_2)
else:
    numero_2 = float(numero_2)

print(f'A soma dos números é: {numero_1 + numero_2}')