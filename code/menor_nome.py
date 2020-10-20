def menor_nome(nomes):
    nome_anterior = 0

    for i in nomes:
        x = i.strip()
        nome_atual = len(x)
        if nome_atual < nome_anterior or nome_anterior == 0:
            nome_anterior = nome_atual
            menor = x.capitalize()

    return menor 
                
            
