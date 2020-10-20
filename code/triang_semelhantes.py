class Triangulo:
    def __init__(self, a, b, c):
        self.a = a
        self.b = b
        self.c = c

    def semelhantes(self, triangulo):
        lista1 = [self.a, self.b, self.c]
        lista2 = [triangulo.a, triangulo.b, triangulo.c]
        lista1_ord = sorted(lista1)
        lista2_ord = sorted(lista2)

        if lista1_ord[0]/lista2_ord[0] == lista1_ord[1]/lista2_ord[1] == lista1_ord[2]/lista2_ord[2]:
            return True
        
        else:
            return False 
                                                                            

        
