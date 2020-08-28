n= int(input("Digite um número inteiro: "))

i = 1
primo = True  

while (i < (n - 1)) and primo:
     i = i + 1
     if (n % i) == 0:
         primo = False

if primo:        
   print ("primo")
else:
   print("não primo")


