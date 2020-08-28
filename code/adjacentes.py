
num = int(input("Digite um número: "))
          
numerosadjacentes = False
resto = 0
valor = 0


while num > 0 and  not numerosadjacentes: 
    resto = num % 10 
    num = num // 10 
    valor = num  % 10
    
    if resto == valor:
       numerosadjacentes = True

if numerosadjacentes: 
    print("sim")
else:
    print("não")

