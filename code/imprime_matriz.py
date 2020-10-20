def imprime_matriz(matriz):
    col = len(matriz[0])
    
    for i in matriz:
        for j in i:
            if j == col:
                print(j, end="")
            else:
                print(j, end=" ")
                
        print()

