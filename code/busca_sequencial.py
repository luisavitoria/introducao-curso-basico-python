def busca(lista, elemento):
    fim = len(lista)

    for i in range(fim):
        if lista[i] == elemento:
            return i
        
    return False 
