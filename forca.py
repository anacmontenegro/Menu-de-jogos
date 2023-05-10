# Importando random:
import random

# Função para jogar:
def jogar_forca():
    mensagem_de_abertura()
    palavra_secreta = sorteando_palavra()
    letras_acertadas = inicializar_letras(palavra_secreta)
    print(letras_acertadas)
    
    enforcou = False
    acertou = False
    erros = 0

    while (not enforcou and not acertou):
        chute = pedir_chute()

        if (chute in palavra_secreta):
            index = 0
            for letra in palavra_secreta:
                if (chute == letra):
                    letras_acertadas[index] = letra
                index += 1
        else:
            erros += 1
            desenhar_forca(erros)
            if (erros <= 5):
                print("Ops, você errou! Faltam {} tentativas.".format(7-erros))
            if (erros == 6):
                print("Ops, você errou! Falta {} tentativa.".format(7-erros))

        enforcou = erros == 7
        acertou = "_" not in letras_acertadas
        print(letras_acertadas)

    if (acertou):
        print("Parabéns, você venceu o jogo!")
    else:
        print("Tentativas esgotadas!\nA palavra secreta era: {}".format(palavra_secreta))
    
    print("Fim do jogo")

# Função para imprimir mensagem de boas vindas:
def mensagem_de_abertura():
    print("*********************************")
    print("***Bem-vindo ao Jogo da Forca!***")
    print("*********************************")

# Função para definir a palavra secreta:
def sorteando_palavra():
    arquivo = open("palavrasforca.txt", "r")
    palavras = []
    for linha in arquivo:
        linha = linha.strip()
        palavras.append(linha)
    arquivo.close()

    numero = random.randrange(0, len(palavras))
    palavra_secreta = palavras[numero].upper()
    return palavra_secreta

# Função para exibir as letras acertadas:
def inicializar_letras(palavra):
    return ["_" for letra in palavra]

# Função para o jogador chutar:
def pedir_chute():
    chute = input("Digite uma letra: ")
    chute = chute.strip().upper()
    return chute

# Função para desenhar forca:
def desenhar_forca(erros):
    print("  _______     ")
    print(" |/      |    ")

    if(erros == 1):
        print(" |      (_)   ")
        print(" |            ")
        print(" |            ")
        print(" |            ")

    if(erros == 2):
        print(" |      (_)   ")
        print(" |      \     ")
        print(" |            ")
        print(" |            ")

    if(erros == 3):
        print(" |      (_)   ")
        print(" |      \|    ")
        print(" |            ")
        print(" |            ")

    if(erros == 4):
        print(" |      (_)   ")
        print(" |      \|/   ")
        print(" |            ")
        print(" |            ")

    if(erros == 5):
        print(" |      (_)   ")
        print(" |      \|/   ")
        print(" |       |    ")
        print(" |            ")

    if(erros == 6):
        print(" |      (_)   ")
        print(" |      \|/   ")
        print(" |       |    ")
        print(" |      /     ")

    if (erros == 7):
        print(" |      (_)   ")
        print(" |      \|/   ")
        print(" |       |    ")
        print(" |      / \   ")

    print(" |            ")
    print("_|___         ")
    print()

# Inicializando:
if(__name__ == "__main__"):
    jogar_forca()
