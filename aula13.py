"""
While = repetições (enquanto)
Loop infinito = quando um código não tem fim
"""

condicao = True

while condicao:
    nome = input('Qual o seu nome: ')
    print(f'Seu nome é {nome}')

    if nome == 'sair':
        break


while False:
    print('EITA')
print('Acabou')