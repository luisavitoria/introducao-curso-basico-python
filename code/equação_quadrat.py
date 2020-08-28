a= float(input("Digite o valor da constante 'a': "))
b = float(input("Digite o valor da constante 'b': "))
c= float(input("Digite o valor da constante 'c': "))

import math 
delta= (b**2)- (4*a*c)
x1= (-b + math.sqrt(abs(delta)))/ (2*a)
x2= (-b - math.sqrt(abs(delta)))/ (2*a)

if delta == 0:
    print ("a raiz desta equação é", x1)

elif delta > 0:
    if x1>x2:
      print ("as raízes da equação são",x2,"e", x1)
    else:
      print ("as raízes da equação são",x1,"e", x2)
        

else:
    print ("esta equação não possui raízes reais")
