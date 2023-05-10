# Importando random:
import random

# Função para jogar:
def jogar_adivinhacao():

    # Boas vindas:
    print("*********************************")
    print("Bem-vindo ao Jogo da Adivinhação!")
    print("*********************************")

    # Sorteando o número secreto:
    numero_secreto = random.randrange(1, 101)

    # Tentativas e pontos (valores iniciais):
    total_de_tentativas = 0
    pontos = 1000

    # Escolhendo o nível do jogo:
    print("Qual o nível de dificuldade?")
    print("(1) Fácil (2) Médio (3) Difícil")

    nivel = int(input("Defina o nível: "))

    if nivel == 1:
        total_de_tentativas = 10
    elif nivel == 2:
        total_de_tentativas = 7
    else:
        total_de_tentativas = 5

    # Jogando:
    for rodada in range(1, total_de_tentativas + 1):
        print("- Tentativa {} de {}".format(rodada, total_de_tentativas))
        chute_str = input("Digite um número entre 1 e 100: ")
        chute = int(chute_str)
        print("Você digitou:", chute)

        if (chute < 1 or chute > 100):
            print("O número precisa ser entre 1 e 100.")
            continue

        # Verificando se chute foi maior ou menor que o número secreto:
        acertou = chute == numero_secreto
        maior = chute > numero_secreto
        menor = chute < numero_secreto
        pontos_perdidos = abs(numero_secreto - chute)
        pontos = pontos - pontos_perdidos

        if (acertou):
            print("Você acertou e fez {} pontos!".format(pontos))
            break
        else:
            if (maior):
                print("Você errou! O seu chute foi maior do que o número secreto.")
                if (rodada == total_de_tentativas):
                    print("O número secreto era {}. Você perdeu o jogo.".format(numero_secreto))
            elif (menor):
                print("Você errou! O seu chute foi menor do que o número secreto")
                if (rodada == total_de_tentativas):
                    print("O número secreto era {}. Você perdeu o jogo.".format(numero_secreto))
    
    # Finalizando:
    print("Fim do jogo")

# Iniciando:
if(__name__ == "__main__"):
    jogar_adivinhacao()
