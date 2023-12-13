import random

def jogar():
    print("*******************************")
    print("Bem vindo ao jogo de advinhação")
    print("*******************************")

    numero_secreto = (random.randrange(1, 101))
    total_de_tentativas = 0
    pontos = 1000

    print("Qual nivel de dificuldade você vai querer?")
    print("Fácil (1) Médio (2) Difícil (3)")

    nivel = int(input("Defina o nível: "))
    if(nivel == 1):
        total_de_tentativas = 20
    elif(nivel == 2):
        total_de_tentativas = 10
    else:
        total_de_tentativas = 5

    rodada = 1
    mensagem = "Digite um número entre 1 e 100: "

    for rodada in range ( 1,total_de_tentativas + 1):
        print("Tentativa {} de {}".format(rodada, total_de_tentativas))
        print(mensagem)
        chute = int(input("Digite Seu número: "))

        if (chute < 1 or chute > 100):
            continue

        acertou = chute == numero_secreto
        maior   = chute > numero_secreto
        menor   = chute < numero_secreto

        if(acertou):
            print("Parabéns você acertou e fez {} " .format(pontos))
            break
        else:
            if (maior):
                print("<<")
            elif(menor):
                print(">>")
            pontos_perdidos = abs(numero_secreto - chute)
            pontos = pontos - pontos_perdidos

    print("Fim de jogo!")

if(__name__ == "__main__"):
    jogar()