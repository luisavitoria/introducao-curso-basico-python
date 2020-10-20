def dimensoes(matriz):
    lin = len(matriz)
    col = len(matriz[0])
    
    dimensao = [lin, col]
    
    return dimensao

def soma_matrizes(m1, m2):
    dim1 = dimensoes(m1)
    num_linhas1 = dim1[0]
    num_colunas1 = dim1[1]
    dim2 = dimensoes(m2)
    
    matriz_soma = []

    if dim1 != dim2:
        
        return False

    else:
        for i in range(num_linhas1):
            linha = []
            for j in range(num_colunas1):
                soma = m1[i][j] + m2[i][j]
                linha.append(soma)
                
            matriz_soma.append(linha)
                
        return matriz_soma
    

