def vogal(v):
    if v == "a" or v == "A" or v == "e" or v == "E" or v == "i" or v== "I" or v == "O" or v == "o" or v == "u" or v == "U":
        return True
    else:
        return False 


v = str(input("Digite uma letra: "))
f = vogal(v)
print(f)
