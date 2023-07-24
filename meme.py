perguntas = [
    {
        'Pergunta': 'me beija aikkkkkkkkkkk',
        'Opções': ['sim obvio lindo', 'talvez', 'nao', 'nunca'],
        'Resposta': 'sim obvio lindo',
    },
]

print('Pergunta:',perguntas[0]['Pergunta'])
print('Opções:',
      '\n01)',perguntas[0]['Opções'][0],
      '\n02)',perguntas[0]['Opções'][1],
      '\n03)',perguntas[0]['Opções'][2],
      '\n04)',perguntas[0]['Opções'][3])

resposta_1 = input('Escolha uma opção iandra mocreia: ')

if resposta_1.isdigit() and resposta_1 in ['1', '01']:
    print('GAY?🤨🌈?')
else:
    print('Errou, sua fudida tem que falar sim')
