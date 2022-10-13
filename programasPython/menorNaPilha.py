from ast import Str
from tokenize import String


def valorMinimo(listaPresentes, numOperacoes):
    aux = 0
    for i in range(numOperacoes):
        if listaPresentes[i] >= aux:
            aux = listaPresentes[i]
    return aux

numOperacoes = int(input())
listaPresentes = []

for i in range(numOperacoes):
    menu = input()
    
    if String.is_integer(int(menu[-2::])):
        grauDeDiversao = int(menu[-2::])
        if menu == "PUSH":
            listaPresentes.append(grauDeDiversao)
    else:
        if menu == "MIN":
            print(valorMinimo(listaPresentes, numOperacoes))
        if menu == "POP":
            listaPresentes.pop()
        else:
            print("Erro!")