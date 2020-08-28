

numero= int(input("Digite um número inteiro: "))

soma=0
resto= 0
            
while numero>0:
    resto= numero%10
    soma= resto + soma
    numero= numero//10

print (soma)


