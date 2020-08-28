n = int(input("Digite o valor de n: "))

fatorial = 1

if (n <= 1):
 print(fatorial)
 
else:
   while (n - 1) > 0:
      a = n*(n-1)
      n = n - 2
      fatorial = fatorial * a
   print(fatorial)



  
    
