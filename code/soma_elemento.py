def main():    
    x = 1
    lista = []
    while x != 0:
        x = int(input("Digite um número inteiro: "))
        lista.append(x)
    del lista[-1]

    return soma(lista)
    
    
def soma_elementos(lista):
    s = 0
    for i in range (len(lista)):
        s = s + lista[i]
        
    return s



print(main())
