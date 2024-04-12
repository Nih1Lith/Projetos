import random
def jogar():

    print("********")
    print("Bem Vindo ao Jogo de Adivinhação!")
    print("********\n")
    
    total_de_tentativas = 0
    rodada = 1
    numero_secreto = random.randrange(1,101)
    pontos = 1000
    
    print("(1) Fácil (2) Médio (3) Difícil")
    nivel = int(input("Escolha uma dificuldade:"))
    
    if (nivel == 1):
        total_de_tentativas = 20
    elif (nivel == 2):
        total_de_tentativas = 10
    else:
        total_de_tentativas = 5
    
    for rodada in range (1,total_de_tentativas + 1):
        print("Tentativa {} de {}".format(rodada, total_de_tentativas))
        
        chute_str = input("Digite um número ente 1 e 100:")
        chute = int(chute_str)
        if (chute < 1 or chute > 100):
            print("Digite um número entre 1 e 100\n")
            continue
            
        acertou = chute == numero_secreto
        maior = chute > numero_secreto
        menor = chute < numero_secreto
        pontos_perdidos = abs(numero_secreto - chute)
        pontos = pontos - pontos_perdidos
        
        if (acertou):
            print("\nVocê acertou! Seus pontos são {}".format(pontos))
            break
        elif (maior):
            print("Você errou! Seu chute foi maior\n")
            if (rodada == total_de_tentativas):
                print("As tentativas acabaram, o número secreto é {} e sua quantidade de pontos é {}".format(numero_secreto, pontos))
        elif (menor):
            print("Você errou! Seu chute foi menor\n")
            if (rodada == total_de_tentativas):
                print("As tentativas acabaram, o número secreto é {} e sua quantidade de pontos é {}".format(numero_secreto, pontos))
                
        pontos_perdidos = numero_secreto - chute
        pontos = pontos - pontos_perdidos
       
    print("Fim de Jogo")
    
if(__name__ == "__main__"):
    jogar()