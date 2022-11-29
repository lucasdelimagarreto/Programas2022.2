class Nodo:
    def __init__(self,data):
        self.data = data
        self.esquerda = None
        self.direita = None
        self.grau = 0

    def Ordem(self):
        if self:
            if self.esquerda:
                self.esquerda.Ordem()
            print(str(self.data), end = ' ')
            if self.direita:
                self.direita.Ordem()

    def grauEmOrdem(self):
        if self:
            if self.esquerda:
                self.esquerda.grauEmOrdem()
            print(str(self.grau), end = ' ')
            if self.direita:
                self.direita.grauEmOrdem()

class Arvore:
    def __init__(self):
        self.raiz = None

    def inserir(self, data):
        if self.raiz:
            return self.raiz.insere(data)
        else:
            self.raiz = Nodo(data)
            return True

    def nosArvore(self):
        print()
        if (self.raiz != None):
            print('Inorder: ')
            self.raiz.Ordem()

    def grauNosArvore(self):
        print()
        if (self.raiz != None):
            print('Inorder: ')
            self.raiz.grauEmOrdem()
    
    def insercao(self, data):
        if (self.data == data):
            return False
        elif self.data < data:
            if self.direita:
                return self.direita.insere(data)
            else:
                self.grau += 1
                self.direita = Nodo(data)
                return True
        else:
            if self.esquerda:
                return self.esquerda.insere(data)
            else:
                self.grau += 1
                self.esquerda = Nodo(data)
                return True
    
    def nosFolha(self,atual):
        if atual == None:
            return 0
        elif (atual.esquerda == None and atual.direita == None):
            return 1
        else:
            return self.nosFolha(atual.esquerda) + self.nosFolha(atual.direita) 

novaArvore = Arvore()
var = 0
novaArvore.inserir(100)
novaArvore.inserir(2002)
novaArvore.inserir(500)
novaArvore.inserir(400)
novaArvore.inserir(250)
novaArvore.inserir(800)
novaArvore.inserir(700)
novaArvore.inserir(1500)
novaArvore.inserir(1300)
novaArvore.nosArvore()
novaArvore.grauNosArvore()
print()
print(novaArvore.nosFolha(novaArvore.raiz))
print()