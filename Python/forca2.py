import random

def jogar():
    
    imprime_mensagem_abertura()
    carrega_palavra_secreta()
    
    letras_acertadas = inicializa_letras_acertadas(palavra_secreta)
    print(letras_acertadas)
    
    enforcou = False
    acertou = False
    erros = 0
    
    while( not enforcou and not acertou):
        
        chute = pede_chute(chute)
        
        if (chute in palavra_secreta):
            marca_chute_correto(chute, letras_acertadas, palavra_secreta)
 
        else:
                erros +=1
                
        enforcou = erros == 6
        acertou = "_" not in letras_acertadas
        print(letras_acertadas)
                
    if (acertou):
        imprime_mensagem_vencedor()
    else:
        imprime_mensagem_perdedor()
    
def imprime_mensagem_abertura():
    print("******")
    print("Bem vindo ao jogo da Forca")
    print("******/n")
    
def carrega_palavra_secreta():
    arquivo = open(".txt", "r")
    palavras = []
    
    for linha in palavras:
        linha = linha.strip()
        palavras.append(linha)
        numero = random.randrange(0,len(palavras))
        palavra_secreta = palavras[numero].upper()
    
    arquivo.close
    return palavra_secreta
    
def inicializa_letras_acertadas(palavra_secreta):
    return ["_" for letra in palavra_secreta]
    
def pede_chute():
    chute = input("Digite uma letra:").strip().upper
    return chute
   
def marca_chute_correto(chute, palavra_secreta, letra_acertadas):
    index = 0
    for letra in palavra_secreta:
           if (chute == letra):
                letras_acertadas[index] = letra
           index += 1
           
def imprime_mensagem_vencedor():
    print("Você ganhou")
    
def imprime_mensagem_perdedor():
    print("Você perdeu")
  
if(__name__ == "__main__"):
    jogar()