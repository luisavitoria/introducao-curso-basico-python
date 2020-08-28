a= int(input("Digite o valor da constante 'a': "))
b = int(input("Digite o valor da constante 'b': "))
c= int(input("Digite o valor da constante 'c': "))

import math 
delta= (b**2)- (4*a*c)

if delta< 0:
    print ("As raízes da equação não são reais.")
import math 
else:
    
x1= (-b + math.sqrt(delta))/ (2*a)
x2= (-b - math.sqrt(delta))/ (2*a)

else delta == 0:
    print ("A raiz única da equação é:", x1)

else:
    print ("As raízes da equação são:",x1,"e", x2)


