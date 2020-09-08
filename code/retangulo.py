
l = int(input("digite a largura: "))
a = int(input("digite a altura: "))

linha = 1
coluna = 1

while coluna <= a:
    while linha <= l:
        print("#", end = "")
        linha = linha + 1
    print()
    linha = 1
    coluna = coluna + 1
