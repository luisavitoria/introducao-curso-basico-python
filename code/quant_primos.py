def n_primos(n):
    #n = int(input("Digite um número >= 2: "))

    i = 2
    primo = True
    cont = 0
    k = 2
        

    while (i <= n):
        if i == 2:
            primo == True
            cont = cont + 1
            
        else:
            while (k < i):
                if (i % k) != 0:
                    primo = True
                else:
                    primo = False
                    break 
                k = k + 1
                
            if primo:        
                cont = cont + 1

        k = 2
        i = i + 1
        
    return cont
    print(cont)

