n= int(input("Digite um número inteiro: "))

i = 2
primo = True  

while (i < n) and primo:
     if (n % i) == 0:
         primo = False
     i = i + 1

if primo:        
   print ("primo")
else:
   print("não primo")
