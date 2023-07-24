pontuação = 0
perguntas = [
    {
        'Pergunta': 'Quanto é 2+2?',
        'Opções': ['1', '3', '4', '5'],
        'Resposta': '4',
    },
    {
        'Pergunta': 'Quanto é 5*5?',
        'Opções': ['25', '55', '10', '51'],
        'Resposta': '25',
    },
    {
        'Pergunta': 'Quanto é 10/2?',
        'Opções': ['4', '5', '2', '1'],
        'Resposta': '5',
    },
]

print('Pergunta:',perguntas[0]['Pergunta'])
print('Opções:',
      '\n01)',perguntas[0]['Opções'][0],
      '\n02)',perguntas[0]['Opções'][1],
      '\n03)',perguntas[0]['Opções'][2],
      '\n04)',perguntas[0]['Opções'][3])

resposta_1 = input('Escolha uma opção: ')

if resposta_1.isdigit() and resposta_1 in ['3', '03']:
    print('Acertou')
    pontuação += 1
else:
    print('Errou')

print('Pergunta:',perguntas[1]['Pergunta'])
print('Opções:',
      '\n01)',perguntas[1]['Opções'][0],
      '\n02)',perguntas[1]['Opções'][1],
      '\n03)',perguntas[1]['Opções'][2],
      '\n04)',perguntas[1]['Opções'][3])

resposta_1 = input('Escolha uma opção: ')

if resposta_1.isdigit() and resposta_1 in ['1', '01']:
    print('Acertou')
    pontuação += 1
else:
    print('Errou')

print('Pergunta:',perguntas[2]['Pergunta'])
print('Opções:',
      '\n01)',perguntas[2]['Opções'][0],
      '\n02)',perguntas[2]['Opções'][1],
      '\n03)',perguntas[2]['Opções'][2],
      '\n04)',perguntas[2]['Opções'][3])

resposta_1 = input('Escolha uma opção: ')

if resposta_1.isdigit() and resposta_1 in ['2', '02']:
    print('Acertou')
    pontuação += 1
else:
    print('Errou')


print(f'Parabens, acertou {pontuação} de 3')


