def remove_repetidos(lista):
    a = []
    for i in lista:
        if i not in a:
            a.append(i)

    a.sort()
    return a

def main():    
    x = 1
    lista = []
    while x != 0:
        x = int(input("Digite um número inteiro: "))
        lista.append(x)
    del lista[-1]
    
    return remove_repetidos(lista)


print(main())

