def maximo(x,y,z):
    if (x > y) and (x > z):
        return x

    elif (y > x) and (y > z):
        return y

    elif (z > x) and (z > y):
        return z

x = int(input("Digite um número:"))
y = int(input("Digite um número:"))
z = int(input("Digite um número:"))

print(maximo(x,y,z))
