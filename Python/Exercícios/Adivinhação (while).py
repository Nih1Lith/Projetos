print("********")
print("Bem Vindo ao Jogo de Adivinhação!")
print("********\n")

total_de_tentativas = 3
rodada = 1
numero_secreto = 42

while rodada <= total_de_tentativas:
    print("Tentativa {} de {}".format(rodada, total_de_tentativas))
    
    chute_str = input("Digite um número:")
    chute = int(chute_str)
    acertou = chute == numero_secreto
    maior = chute > numero_secreto
    menor = chute < numero_secreto
    
    if (acertou):
        print("Você acertou!")
    elif (maior):
        print("Você errou! Seu chute foi maior\n")
    else:
        print("Você errou! Seu chute foi menor\n")
   
    
    rodada = rodada +1
print("Fim de Jogo")