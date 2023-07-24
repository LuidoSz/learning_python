Horario = input('Digite seu horario: ')
Horario_int = int(f'{Horario}')

if Horario_int < 12:
    print('Bom dia!')
elif Horario_int < 18:
    print('Boa Tarde!')
else:
    print('Boa noite!')


