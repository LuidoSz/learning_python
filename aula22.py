frase = 'O python é uma linguagem de programação'\
    'multiparadigma'\
    'Python foi criado por Guido van rossum '

print(frase.count('a'))


i = 0
qtd_apareceu_mais_vezes = 0
letra_apareceu_mais_vezes = ''
while i < len(frase):
    letra_atual = frase[i]
    
    if letra_atual == ' ':
        i += 1
        continue
    quantas_vezes_letra_apareceu = frase.count(letra_atual)

    if qtd_apareceu_mais_vezes  < quantas_vezes_letra_apareceu:
        qtd_apareceu_mais_vezes  = quantas_vezes_letra_apareceu
        letra_apareceu_mais_vezes = letra_atual
    i += 1
print('A letra que apareceu mais vezes foi '
    f'{letra_apareceu_mais_vezes} que apareceu '
    f'{quantas_vezes_letra_apareceu}x')