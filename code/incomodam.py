def incomodam(n):
    frase = "incomodam"
    s = " "
    
    if n == 1:
        return frase
        
    if n > 1 and n is int :
        a = frase + s + incomodam(n-1)
        return a

    else:
        return s



 
