alfabeto = "abcdefghijklmnopqrstuvxyz"
aux2 = len(alfabeto)

def decodifica(chave, string):
    chave %= aux2
    new_string = ""
    for c in string:
        aux = alfabeto.find(c.lower())
        if (aux != -1):
            new = aux - chave
            if (new < 0):
                new = aux2 + new
            new_string += alfabeto[new]
        else: 
            new_string += c
    return new_string

def codifica(chave, string):
    chave %= aux2
    new_string = ''
    for c in string:
        aux = alfabeto.find(c.lower())
        if (aux != -1):
            new_string += alfabeto[(aux + chave) % (aux2+1)]
        else: 
            new_string += c
    return new_string

while (True):
    print("\n1 - Codificar mensagem \n2 - Decodificar mensagem \n3 - Sair \n")
    while (True):
        x = input('Escolha: ')
        if (x in '123'): 
            break

    if (x == "3"): break
    string = input("Mensagem: ")
    while (True):
        try:
            chave = int(input("Chave: "))
        except:
            continue
        else: 
            break

    print("Resultado: ", end="")
    if (x == "1"): 
        print(codifica(chave, string))
    elif (x == "2"): 
        print(decodifica(chave, string))
    else:
        print("Algo de errado não está certo!")