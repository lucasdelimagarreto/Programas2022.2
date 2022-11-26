def pedeInfo(aux):
        if(aux == 1):
            nome = input("Digite nome do aluno: ")
            return nome
        else:
            disciplina = input("Digite a disciplina do aluno: ")
            return disciplina
            
class Disciplinas:
    
    def __init__(self, nomeDisc: str, nota1: float, nota2: float):
        self.__nomeDisc = nomeDisc
        self.__nota1 = nota1
        self.__nota2 = nota2

    def get_nomeDisc(self):
        return self.__nomeDisc

    def set_nomeDisc(self, nomeDisc):
        self.__nomeDisc = nomeDisc

    def get_nota1(self):
        return self.__nota1

    def set_nota1(self, nota1):
        self.__nota1 = nota1

    def get_nota2(self):
        return self.__nota2
    
    def set_nota2(self, nota2):
        self.__nota2 = nota2

class Node:

    def __init__(self, aluno):
        self.aluno = aluno 
        self.disciplinas = []  
        self.next = None
        self.anterior = None

class List:

    def __init__(self):
        self.front = None 
        #self.rear = None
        self.__tamanho = 0
    
    def enqueueAluno(self, aluno):
        aux = self.front
        anterior = None
        stop = False
        
        while aux != None and not stop:
            
            if aux.aluno > aluno:
                stop = True
            
            else:
                anterior = aux
                aux = aux.next

        temp = Node(aluno)
        
        if anterior == None:
            temp.next = self.front
            self.front = temp
        
        else:
            temp.next = aux
            anterior.next = temp
        
        self.__tamanho += 1

    def buscaAluno(self,nome):   
        if (self.__tamanho == 1):
            if(nome == self.front.aluno):
                return self.front
            else:
                return False
        aux = self.front
        stop = False
        posicao = 0
        fim = (self.__tamanho - 1)  
        atual = (fim/2)
        while(not stop):
            if (atual > 0):
                for i in range (atual):
                    aux = aux.next
                    posicao += 1             
            else:
                for i in range (atual):
                    aux = aux.anterior
                    posicao -= 1         
            if (aux.aluno == nome):            
                return aux
            else:
                if (nome > aux.aluno):
                    atual = (fim - posicao)/2             
                else:
                    atual = (-fim + posicao)/2
                if (isinstance(atual,float)):
                    atual = int(atual + 0.5)        
            if (posicao == 0 or posicao == fim):
                stop = True
        return False

    def tamanhoDaLista(self):
        return self.__tamanho

    def inserirDisciplina(self, nome):
            
        objDisciplina = Disciplinas()
        objDisciplina.set_nomeDisc(input("Digite o nome da disciplina: "))
        stop = self.front
        while stop != None:
            if stop.aluno == nome:
                stop.disciplinas.append(objDisciplina)
                stop.disciplinas.sort()
                
            stop = stop.next

    def removerDisciplina(self, disciplina, nome):

        objDisciplina = Disciplinas()
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
            
        
    def inserirNota(self, disciplina, nome):

        objDisciplina = Disciplinas()
        stop = self.front
        while stop != None:

            if stop.aluno == nome:

                for i in range(len(stop.disciplinas)):

                    if (stop.disciplinas[i] == disciplina):

                        if (objDisciplina.get_nota1 != None and objDisciplina.get_nota2 != None):
                            print("Você já cadastrou duas notas nesta disciplina, caso queira modificar essas notas volte ao menu!\n")
                        
                        else:
                            while(aux):
                                nota = int(input("Qual dota deseja adicionar 1a ou 2a:"))

                                if(nota == 1):
                                    objDisciplina = stop.disciplinas[i]
                                    objDisciplina.set_nota1 = nota
                                    stop.disciplinas[i] = objDisciplina.set_nota1
                                    aux = False

                                elif(nota == 2):
                                    objDisciplina = stop.disciplinas[i]
                                    objDisciplina.set_nota2 = nota
                                    stop.disciplinas[i] = objDisciplina.set_nota2
                                    aux = False

                                else:
                                    print("Digite um numero entre 1 e 2")
                                    aux = True
            stop = stop.next

    def removerNota(self, disciplina, nome):

        objDisciplina = Disciplinas()
        stop = self.front
        while stop != None:
            if stop.aluno == nome:
                for i in range(len(stop.disciplinas)):
                    if (stop.disciplinas[i] == disciplina):
                        print(stop.disciplinas[i])
                        while(aux):
                            nota = int(input("Qual dota deseja remover 1a ou 2a:"))
                            if(nota == 1):
                                objDisciplina.set_nota1 = None
                                aux = False
                            elif(nota == 2):
                                objDisciplina.set_nota2 = None
                                aux = False
                            else:
                                print("Digite um numero entre 1 e 2")
                                aux = True
            stop = stop.next

    def removeAluno(self, aluno):
        if self.isEmpty():
            print("O Controle Acadêmico está vazio, não há alunos cadastrados")
        elif self.front.aluno == aluno:
            self.front = self.front.next
        else:
            anterior = None
            aux = self.front
            
            while aux and aux.aluno != aluno:
                anterior = aux
                aux = aux.next
            
            if aux:
                anterior.next = aux.next
            
            else:
                anterior.next = None

            self.__tamanho -= 1
            

    def isEmpty(self):
        return self.front == None 
    
    def __tamanho(self): 
        return self.__tamanho

    def front(self):
        return self.front

    #def rear(self):
    #   return self.rear

    def visualizarMediaEmDisciplina(self, aluno, disciplina):
        output = ""
        
        if self.front:
            aux = self.front
            output += ""

            while (aux):
                if (aux.aluno == aluno):
                    for i in range(len(aux.disciplinas)):
                        for j in range( len( aux.disciplinas[i] ) ):
                            if (aux.disciplinas[i][j] == disciplina):
                                if (len(aux.disciplinas[j]) > 2):
                                    media = (aux.disciplinas[i][1] + aux.disciplinas[i][2] ) / 2
                                    output += "[Aluno: {}]\n[Média em {}: {}]\n".format(aux.aluno, disciplina, media)
                                else:
                                    return "O Aluno não tem as duas notas cadastradas nessa disciplina"
                            
                            return output
            
            aux = aux.next
    
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

    if (choose == 1):

        aluno = pedeInfo(1)
        controleAcademico.enqueueAluno(aluno)
        print("Aluno cadastrado")
        print()

        continuaMenu = int(input("Deseja sair do Programa agora?\nDigite 0 para sim e 1 para não: "))

    elif (choose == 2):

        nomeDisciplina = input("Digite o nome da disciplina: ")
        aluno = input("Digite o nome do aluno cadastrado: ")
        controleAcademico.inserirDisciplina(nomeDisciplina, controleAcademico.pedeInfo(1))
        print()

        continuaMenu = int(input("Deseja sair do Programa agora?\nDigite 0 para sim e 1 para não: "))

    elif (choose == 3):

        disciplina = input("digite o nome da disciplina: ")
        nota = int(input("Digite a nota: "))
        controleAcademico.inserirNota(nota, controleAcademico.pedeInfo(2), controleAcademico.pedeInfo(1))
        print()

        continuaMenu = int(input("Deseja sair do Programa agora?\nDigite 0 para sim e 1 para não: "))

    elif (choose == 4):
        controleAcademico.removeAluno(controleAcademico.pedeInfo(1))
        print()

        continuaMenu = int(input("Deseja sair do Programa agora?\nDigite 0 para sim e 1 para não: "))
    
    elif (choose == 5):
        controleAcademico.removerDisciplina(controleAcademico.pedeInfo(2) , controleAcademico.pedeInfo(1))
        print()

        continuaMenu = int(input("Deseja sair do Programa agora?\nDigite 0 para sim e 1 para não: "))

    elif (choose == 6):
        print("remover nota da disciplina do aluno")
        controleAcademico.removerNota(controleAcademico.pedeInfo(2), controleAcademico.pedeInfo(1))
        print()

        continuaMenu = int(input("Deseja sair do Programa agora?\nDigite 0 para sim e 1 para não: "))
    
    elif (choose == 7):
        print("Atualizar dados do aluno, no nosso caso o nome dele apenas")
        controleAcademico.buscaAluno(controleAcademico.pedeInfo(1))
        print()

        continuaMenu = int(input("Deseja sair do Programa agora?\nDigite 0 para sim e 1 para não: "))

    elif (choose == 8):
        print("Atualizar disciplina do aluno, no caso o nome da disciplina")
        print()

        continuaMenu = int(input("Deseja sair do Programa agora?\nDigite 0 para sim e 1 para não: "))

    elif (choose == 9):
        print("Atualizar nota de disciplina de aluno")
        print()

        continuaMenu = int(input("Deseja sair do Programa agora?\nDigite 0 para sim e 1 para não: "))
    
    elif (choose == 10):

        aluno = input("Digite o nome do aluno: ")
        disciplina = input("digite o nome da disciplina: ")

        print(controleAcademico.visualizarMediaEmDisciplina(controleAcademico.pedeInfo(1), controleAcademico.pedeInfo(2)))
        print()

        continuaMenu = int(input("Deseja sair do Programa agora?\nDigite 0 para sim e 1 para não: "))
    
    elif (choose == 11):
        print("Visualizar os nomes dos alunos que estão com média menor que 7")
        print()

        continuaMenu = int(input("Deseja sair do Programa agora?\nDigite 0 para sim e 1 para não: "))

    elif (choose == 12):
        print("Visualizar os nomes dos alunos que estão com média maior ou igual a 7")
        print()

        continuaMenu = int(input("Deseja sair do Programa agora?\nDigite 0 para sim e 1 para não: "))

    elif (choose == 13):

        aluno = input("Digite o nome do aluno: ")
        print(controleAcademico.visualizacaoCompletaDeAluno(controleAcademico.pedeInfo(1)))
        print()

        continuaMenu = int(input("Deseja sair do Programa agora?\nDigite 0 para sim e 1 para não: "))
    
    else:
        print("Digite um número válido!")