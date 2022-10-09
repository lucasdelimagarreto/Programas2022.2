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
    if menu == "PUSH":
        grauDeDiversao = int(input())
        listaPresentes.append(grauDeDiversao)
    if menu == "MIN":
        print(valorMinimo(listaPresentes, numOperacoes))
    if menu == "POP":
        listaPresentes.pop()