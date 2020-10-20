def maiusculas(frase):
    string = ""

    for i in frase:
        if ord(i)<= 90 and ord(i) >= 65:
            string = string + i
            
    return string
