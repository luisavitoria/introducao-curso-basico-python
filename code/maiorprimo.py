def e_primo(n):
    i = 2
    primo = True  

    while (i < n) and primo:
        if (n % i) == 0:
            primo = False
        i = i + 1

    return primo
    
# n = int(input("Digite um número inteiro: "))
# f = e_primo(n)
# print(f)

def maior_primo(n):
    primo = e_primo(n)
    
    if primo == True:
        return n

    else:
        while primo == False:
            n = n - 1
            primo = e_primo(n)
            
            if (primo == True):
                return n

# f2 = maior_primo(n)
# print(f2)

