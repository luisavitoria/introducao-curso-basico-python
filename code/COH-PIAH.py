import re

def main():
    ass_cp = le_assinatura()
    textos = le_textos()
    infectado = avalia_textos(textos, ass_cp)

    print("O autor do texto",infectado,"está infectado com COH-PIAH")
    

def le_assinatura():
    '''A funcao le os valores dos tracos linguisticos do modelo e devolve uma assinatura a ser comparada com os textos fornecidos'''
    print("Bem-vindo ao detector automático de COH-PIAH.")
    print("Informe a assinatura típica de um aluno infectado:\n")

    wal = float(input("Entre o tamanho médio de palavra:"))
    ttr = float(input("Entre a relação Type-Token:"))
    hlr = float(input("Entre a Razão Hapax Legomana:"))
    sal = float(input("Entre o tamanho médio de sentença:"))
    sac = float(input("Entre a complexidade média da sentença:"))
    pal = float(input("Entre o tamanho medio de frase:"))
    print()

    return [wal, ttr, hlr, sal, sac, pal]

def le_textos():
    '''A funcao le todos os textos a serem comparados e devolve uma lista contendo cada texto como um elemento'''
    i = 1
    textos = []
    texto = input("Digite o texto " + str(i) +" (aperte enter para sair):")
    print()
    while texto:
        textos.append(texto)
        i += 1
        texto = input("Digite o texto " + str(i) +" (aperte enter para sair):")
        print()

    return textos

def separa_sentencas(texto):
    '''A funcao recebe um texto e devolve uma lista das sentencas dentro do texto'''
    sentencas = re.split(r'[.!?]+', texto)
    if sentencas[-1] == '':
        del sentencas[-1]
    return sentencas

def separa_frases(sentenca):
    '''A funcao recebe uma sentenca e devolve uma lista das frases dentro da sentenca'''
    return re.split(r'[,:;]+', sentenca)

def separa_palavras(frase):
    '''A funcao recebe uma frase e devolve uma lista das palavras dentro da frase'''
    return frase.split()

def n_palavras_unicas(lista_palavras):
    '''Essa funcao recebe uma lista de palavras e devolve o numero de palavras que aparecem uma unica vez'''
    freq = dict()
    unicas = 0
    for palavra in lista_palavras:
        p = palavra.lower()
        if p in freq:
            if freq[p] == 1:
                unicas -= 1
            freq[p] += 1
        else:
            freq[p] = 1
            unicas += 1

    return unicas

def n_palavras_diferentes(lista_palavras):
    '''Essa funcao recebe uma lista de palavras e devolve o numero de palavras diferentes utilizadas'''
    freq = dict()
    for palavra in lista_palavras:
        p = palavra.lower()
        if p in freq:
            freq[p] += 1
        else:
            freq[p] = 1

    return len(freq)

def compara_assinatura(as_a, as_b):
    '''IMPLEMENTAR. Essa funcao recebe duas assinaturas de texto e deve devolver o grau de similaridade nas assinaturas.'''

    i = 0
    diferenca = 0
    
    while i <= 5:
        diferenca = diferenca + abs(as_a[i] - as_b[i])
        i = i + 1
    similaridade = diferenca / 6
    
    return similaridade
    

def calcula_assinatura(texto):
    '''IMPLEMENTAR. Essa funcao recebe um texto e deve devolver a assinatura do texto.'''
    
    lista_palavras = []
    lista_frases = []
    lista_sent = separa_sentencas(texto)
    soma_caracteres_palavras = 0
    soma_caracteres_sentencas = 0
    soma_caracteres_frases = 0

    for sent in lista_sent:
        novas_frases = separa_frases(sent)
        soma_caracteres_sentencas = soma_caracteres_sentencas + len(sent)
        lista_frases.extend(novas_frases)
    for fr in lista_frases:
        novas_palavras = separa_palavras(fr)
        soma_caracteres_frases = soma_caracteres_frases + len(fr)
        lista_palavras.extend(novas_palavras)
    for palavra in lista_palavras:
        soma_caracteres_palavras = soma_caracteres_palavras + len(palavra)

    wal_texto = soma_caracteres_palavras / len(lista_palavras)
    ttr_texto = n_palavras_diferentes(lista_palavras) / len(lista_palavras)
    hlr_texto = n_palavras_unicas(lista_palavras) / len(lista_palavras)
    sal_texto = soma_caracteres_sentencas / len(lista_sent)
    sac_texto = len(lista_frases) / len(lista_sent)
    pal_texto = soma_caracteres_frases / len(lista_frases)

    assinatura = [wal_texto, ttr_texto, hlr_texto, sal_texto, sac_texto, pal_texto]

    return assinatura
    
def avalia_textos(textos, ass_cp):
    '''IMPLEMENTAR. Essa funcao recebe uma lista de textos e uma assinatura ass_cp e deve devolver o numero (1 a n) do texto com maior probabilidade de ter sido infectado por COH-PIAH.'''

    lista_comparacao = []
    
    for cada_texto in textos:
          as_texto = calcula_assinatura(cada_texto)
          comparar = compara_assinatura(as_texto, ass_cp)
          lista_comparacao.append(comparar)

    minimo = min(lista_comparacao)
    texto_infectado = lista_comparacao.index(minimo) + 1

    return texto_infectado

main()
