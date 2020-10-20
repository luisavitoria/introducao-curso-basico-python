def sao_multiplicaveis(m1, m2):
    
    if len(m1) == 1 and len(m2) == 1:
        print (True)

    else:
        num_colunas1 = len(m1[0])
        num_linhas2 = len(m2)
        if num_colunas1 == num_linhas2:
            print(True)

        else:
            print(False) 
        
