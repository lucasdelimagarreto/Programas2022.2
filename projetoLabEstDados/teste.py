def pedeInfo(aux):

        if(aux == 1):
            nome = input("Digite nome do aluno: ")
            return nome
        elif(aux == 2):
            disciplina = input("Digite a disciplina do aluno: ")
            return disciplina
        elif(aux == 3):
            nota = float(input("Digite a nota do aluno: "))
            return nota
        else:
            print("ERROR!")

class Disciplina:

    def __init__(self, nomeDisc: str, nota1: float, nota2: float):
        self.nomeDisc = nomeDisc
        self.nota1 = nota1
        self.nota2 = nota2
        self.proximo = None

class ListaDisciplinas:

    def __init__(self):
        self.frente = None 

    def isEmpty(self):
        return self.frente == None

    def frente(self):
        return self.frente

    def enqueueDisciplina(self):
        novaDisciplina = Disciplina(pedeInfo(2), None, None)
        novaDisciplina.proximo = self.frente
        self.frente = novaDisciplina
    
class Aluno:

    def __init__(self, nomeAluno: str):
        self.nomeAluno = nomeAluno
        self.listaDisciplinas = ListaDisciplinas()

class Node:

    def __init__(self, aluno: Aluno):
        self.aluno = aluno
        self.next = None
        self.anterior = None

class List:

    def __init__(self):
        self.front = None 
        self.__tamanho = 0
    
    def isEmpty(self):
        return self.front == None 

    def __tamanho(self): 
        return self.__tamanho

    def front(self):
        return self.front

    def enqueueAluno(self, aluno: str):
        aux = self.front
        anterior = None
        stop = False

        while aux != None and not stop:

            if aux.aluno.nomeAluno > aluno:
                stop = True

            else:
                anterior = aux
                aux = aux.next

        var = Aluno(aluno)
        temp = Node(var)

        if anterior == None:
            temp.next = self.front
            self.front = temp

        else:
            temp.next = aux
            anterior.next = temp

        self.__tamanho += 1

    def buscaAluno(self,nome):   
        if (self.__tamanho == 1):
            if(nome == self.front.aluno.nomeAluno):
                return self.front
            else:
                return False
        aux = self.front
        stop = False
        posicao = 0
        fim = (self.__tamanho - 1)  
        atual = int(fim/2)
        while(not stop):
            if (atual > 0):
                for i in range (atual):
                    aux = aux.next
                    posicao += 1             
            else:
                for i in range (atual):
                    aux = aux.anterior
                    posicao -= 1         
            if (aux.aluno.nomeAluno == nome):            
                return aux
            else:
                if (nome > aux.aluno.nomeAluno):
                    atual = (fim - posicao)/2             
                else:
                    atual = (-fim + posicao)/2
                    if (isinstance(atual,float)):
                        atual = int(atual + 0.5)        
            if (posicao == 0 or posicao == fim):
                stop = True
        return "Aluno não encontrado"

    def buscaDisciplina(self):

        disciplina = pedeInfo(2)
        aluno = controleAcademico.buscaAluno(pedeInfo(1))
        aux = aluno.aluno.listaDisciplinas.frente

        while(aux != None):
            if (aux.nomeDisc == disciplina):
                return aux
            aux = aux.proximo

    def inserirDisciplina(self, nome):

        aux = controleAcademico.buscaAluno(nome)
        aux.aluno.listaDisciplinas.enqueueDisciplina()

    def removerDisciplina(self, disciplina, nome):

        objDisciplina = Disciplina(None, None, None)
        stop = self.front
        while stop != None:
            if stop.aluno == nome:
                for i in range(len(stop.disciplinas)):
                    objDisciplina = stop.disciplinas[i] 
                    if (objDisciplina.get_nomeDisc == disciplina):

                        stop.disciplinas.pop(i)
                        print("Aluno removido com sucesso da disciplina")

                        return

                print("Esse aluno não está matriculado nessa disciplina, logo não pode ser removido dela")

            stop = stop.next

    def inserirNota(self):

        var = controleAcademico.buscaDisciplina()
        
        while(aux):
            nota = int(input("Qual nota deseja adicionar 1a ou 2a:"))

            if(nota == 1):
                var.nota1 = pedeInfo(3)
                print("A nota foi definida para: ", var.nota1)
                aux = False

            elif(nota == 2):
                var.nota2 = pedeInfo(3)
                print("A nota foi definida para: ", var.nota2)
                aux = False

            else:
                print("Digite um numero entre 1 e 2.")
                aux = True             
    
    def removerNota(self):

        temp = controleAcademico.buscaDisciplina

        if (temp.nota1 == None and temp.nota2 == None):
            print("Voce ja removeu as notas deste aluno!\n")

        else:
            while(aux):
                nota = int(input("Qual nota deseja remover 1a ou 2a:"))

                if(nota == 1):
                    temp.nota1 = None
                    if(temp.nota1 == None):
                        print("A nota foi definida para: 0")
                    aux = False

                elif(nota == 2):
                    temp.nota2 = None
                    print("A nota foi definida para: ", temp.nota2)
                    aux = False

                else:
                    print("Digite um numero entre 1 e 2.")
                    aux = True

    def removeAluno(self, aluno):
        
        if self.isEmpty():
            print("O Controle Acadêmico está vazio, não há alunos cadastrados")
        
        elif self.front.aluno == aluno:
            self.front = self.front.next
        
        else:
            aux = controleAcademico.buscaAluno(aluno)
            aux.anterior.next = aux.next
            aux.next.anterior = aux.anterior
            
            self.__tamanho -= 1

    #def rear(self):
    #   return self.rear

    def visualizarMediaEmDisciplina(self):
        aux = controleAcademico.buscaDisciplina()
        media = aux.aluno.listaDisciplina.nota1 / aux.aluno.listaDisciplina.nota2
        print("A media é: ", media)

    def visualizacaoCompletaDeAluno(self, aluno):
        if self.front:
            aux = self.front

            while (aux):
                if (aux.aluno == aluno):
                    output = "Aluno: {}\nDisciplinas e notas: {}\n".format(aux.aluno, aux.disciplinas)
                    return output       

                aux = aux.next

            return "O Aluno não está cadastrado no controle acadêmico ou você digitou o nome dele errado!"


controleAcademico = List()
choose = -1
continuaMenu = 1

while (continuaMenu != 0):
    print("-" * 70)
    print("Controle Acadêmico")
    print()
    print("1 - Cadastrar aluno\n \n2 - Cadastrar disciplinas\n \n3 - Cadastrar notas em disciplina\n \n4 - Remover aluno\n \n5 - Remover disciplina\n \n6 - Remover nota de disciplina\n \n7 - Atualizar dados do aluno\n \n8 - Atualizar disciplina de aluno\n \n9 - Atualizar nota de disciplina\n \n10 - Visualize a média de um aluno\n \n11 - Visualize quais alunos estão com a média menor que 7\n \n12 - Visualize quais alunos estão com média maior ou igual a 7\n \n13 - Visualize as notas das disciplinas cadastradas em um aluno")
    print("-" * 70)
    choose = int(input("Digite um número: "))

    #1 e para pedir nome e 2 para pedir disciplina  controleAcademico.pedeInfo(X)

    if (choose == 1): #FUNCIONA
        # 1 - Cadastrar aluno
        controleAcademico.enqueueAluno(pedeInfo(1))
        print("Aluno de nome",controleAcademico.front.aluno.nomeAluno, " cadastrado")
        print()

    elif (choose == 2): #FUNCIONA
        # 2 - Cadastrar disciplinas

        aux = controleAcademico.inserirDisciplina(pedeInfo(1))
        print("A disciplina inserida foi: ", aux)
        print()

    elif (choose == 3): #FUNCIONA
        # 3 - Cadastrar notas em disciplina
        print("Cadastrar notas!")
        controleAcademico.inserirNota(pedeInfo(2), pedeInfo(1))
        print()

    elif (choose == 4): 
        # 4 - Remover aluno
        print("Cadastrar notas!")
        controleAcademico.removeAluno(pedeInfo(1))
        print()

    elif (choose == 5):
        # 5 - Remover disciplina

        controleAcademico.removerDisciplina(pedeInfo(2) , pedeInfo(1))
        print()

    elif (choose == 6): #FUNCIONA
        # 6 - Remover nota de disciplina

        print("remover nota da disciplina do aluno")
        controleAcademico.removerNota()
        print()
    
    elif (choose == 7): #FUNCIONA
        # 7 - Atualizar dados do aluno

        print("Atualizar dados do aluno, no nosso caso o nome dele apenas")
        controleAcademico.buscaAluno()
        var = input("Digite o novo nome do aluno: ")
        controleAcademico.front.aluno.nomeAluno = var
        print("O atual nome do al")
        print()

    elif (choose == 8): #FUNCIONA
        # 8 - Atualizar disciplina de aluno

        print("Atualizar disciplina do aluno.(no caso o nome da disciplina)")
        disciplina = controleAcademico.buscaDisciplina()
        disciplina.nomeDisc = pedeInfo(2)
        print("O nome da disciplina foi alterado para: ", disciplina.nomeDisc)
        print()

    elif (choose == 9):
        # 9 - Atualizar nota de disciplina

        print("Atualizar nota de disciplina de aluno")
        controleAcademico.inserirNota()

        print()

    elif (choose == 10):

        aluno = input("Digite o nome do aluno: ")
        disciplina = input("digite o nome da disciplina: ")

        print(controleAcademico.visualizarMediaEmDisciplina(pedeInfo(1), pedeInfo(2)))
        print()
    
    elif (choose == 11):
        print("Visualizar os nomes dos alunos que estão com média menor que 7")
        print()

    elif (choose == 12):
        print("Visualizar os nomes dos alunos que estão com média maior ou igual a 7")
        print()

    elif (choose == 13):

        aluno = input("Digite o nome do aluno: ")
        print(controleAcademico.visualizacaoCompletaDeAluno(pedeInfo(1)))
        print()

    else:
        print("Digite um número válido!")

    continuaMenu = int(input("Deseja sair do Programa agora?\nDigite 0 para sim e 1 para não: "))
