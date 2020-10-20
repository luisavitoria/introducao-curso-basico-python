def encontra_impares(lista):
    lista_impares = []
    
    
    if len(lista) > 0:

        if lista[0] % 2 != 0:
            lista_impares.append(lista[0])

        lista_impares = lista_impares + encontra_impares(lista[1:])
    
        
    return  lista_impares

           
    
