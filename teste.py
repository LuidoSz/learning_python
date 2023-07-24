palavras = "banana"

def selecionar_palavra(palavras):
    # Seleciona aleatoriamente uma palavra da lista
    palavra_secreta = (palavras)
    return palavra_secreta

def jogar_jogo(palavra):
    tentativas = 6
    letras_descobertas = []
    
    while tentativas > 0:
        # Exibe a palavra oculta com as letras já descobertas
        palavra_oculta = ""
        for letra in palavra:
            if letra in letras_descobertas:
                palavra_oculta += letra
            else:
                palavra_oculta += "_"
        
        print("Palavra:", palavra_oculta)
        print("Tentativas restantes:", tentativas)
        
        # Solicita ao jogador uma letra
        letra = input("Digite uma letra: ")
        
        if letra in letras_descobertas:
            print("Você já tentou essa letra. Tente novamente.")
            continue
        
        # Verifica se a letra está presente na palavra secreta
        if letra in palavra:
            letras_descobertas.append(letra)
            if set(palavra) == set(letras_descobertas):
                print("Parabéns! Você adivinhou a palavra secreta:", palavra)
                break
        else:
            tentativas -= 1
            print("Letra errada. Tente novamente.")
    
    if tentativas == 0:
        print("Suas tentativas acabaram. A palavra secreta era:", palavra)

# Seleciona uma palavra aleatória da lista
palavra_secreta = selecionar_palavra(palavras)

# Inicia o jogo
jogar_jogo(palavra_secreta)