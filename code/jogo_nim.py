         
def main():
    print("Bem-vindo ao jogo do NIM! Escolha:\n")
    print("1 - para jogar uma partida isolada")
    print("2 - para jogar um campeonato", end = " ")

    opcao = int(input())
    print()
    
    if opcao == 1:
        print("Voce escolheu uma partida isolada!\n")
        partida()

    else:
        print("Voce escolheu um campeonato!\n")
        campeonato()

def partida():
    n = int(input("Quantas peças? "))
    m = int(input("Limite de peças por jogada? \n"))
    
    k = m + 1
    y = 1
    z = 2

    if (n % k == 0):
        print("Você começa!\n")

        while n != 0:
            numero2 = usuario_escolhe_jogada(n,m)
            n = n - numero2
            if n == 0:
                print("Fim do jogo! O usuário ganhou!\n")
                return y
            numero = computador_escolhe_jogada(n,m)
            n = n - numero
            if n == 0:
                print("Fim do jogo! O computador ganhou!\n")
                return z
            
    else:
        print("Computador começa!\n")
        
        while n != 0:
            numero = computador_escolhe_jogada(n,m)
            n = n - numero
            if n == 0:
                print("Fim do jogo! O computador ganhou!\n")
                return z 
            numero2 = usuario_escolhe_jogada(n,m)
            n = n - numero2
            if n == 0:
                print("Fim do jogo! O usuário ganhou!\n")
                return y

def campeonato():
    i = 1
    y = 0
    z = 0
    while i <= 3:
        print("**** Rodada",i,"****\n")
        x = partida()
        i = i + 1
        if x == 1:
            y = y + 1
        else:
            z = z + 1
            
    print("**** Final do campeonato! ****\n")
    print("Placar: Você",y,"X",z,"Computador")
    
           
def computador_escolhe_jogada(n,m):
    k = m + 1
    i = 1
    retirar = 0
    valor = 0

    if n <= m:
        retirar = n

    else:
        while i <= k :
            i = k * i 
            valor = n - i
            i = i + 1
            if valor <= m:
                retirar = valor
            else:
                retirar = m

    resto = n - retirar

    if retirar == 1:
        print("O computador tirou uma peça.")

    else:
        print("O computador tirou",retirar,"peças.")

    if resto == 1:
        print("Agora resta apenas uma peça no tabuleiro.\n")

    elif (resto != 0) and (resto != 1):
        print("Agora restam",resto,"peças no tabuleiro.\n")

    return retirar

def usuario_escolhe_jogada(n,m):
    a = int(input("Quantas peças você vai tirar? "))
    print()

    while a > m:
        print("Oops! Jogada inválida! Tente de novo.\n")
        a = int(input("Quantas peças você vai tirar? "))
        print()

    b = n - a

    if a == 1:
        print("Você tirou uma peça.")

    else:
        print("Você tirou",a,"peças.")

    if b == 1:
        print("Agora resta apenas uma peça no tabuleiro.\n")

    elif (b != 0) and (b != 1):
        print("Agora restam",b,"peças no tabuleiro.\n")

    return a

main()

    


        
    
        
            


    

  
    

        
            
        

