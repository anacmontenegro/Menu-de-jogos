# Importando arquivos dos jogos:
import forca
import adivinhacao

# Função para escolher o jogo: 
def jogos():

    # Boas vindas e opções:
    print("*********************************")
    print("*********Escolha o jogo:*********")
    print("*********************************")

    print("(1) Forca (2) Adivinhação")
    jogo = int(input("Qual jogo você quer jogar? "))

    # Escolhendo um jogo:
    if (jogo == 1):
        print("Jogo selecionado: Forca")
        forca.jogar_forca()
    elif (jogo == 2):
        print("Jogo selecionado: Adivinhação")
        adivinhacao.jogar_adivinhacao()

# Inicializando:
if(__name__ == "__main__"):
    jogos()
