
g = int(input("digite a largura: "))
a = int(input("digite a altura: "))

linha = 1
coluna = 1

while linha <= a:
    if linha == 1 or linha == a:
        while coluna <= g:
            print("#", end = "")
            coluna = coluna + 1
        print()
    else:
        while coluna <= g:
            if coluna == 1 or coluna == g:
                print("#", end = "")
            else:
                print(" ", end = "")
            coluna = coluna + 1
        print()

    linha = linha + 1
    coluna = 1
