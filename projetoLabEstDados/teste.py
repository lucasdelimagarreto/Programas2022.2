class Disciplinas:
    
    def __init__(self, nomeDisc: str, nota1: float, nota2: float) -> None:
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
        if self.__tamanho == 1:
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
            if (posicao == 0 and posicao == fim):
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
            
        
    def inserirNota(self, nota, disciplina, nome):
        stop = self.front
        while stop != None:
            if stop.aluno == nome:
                for i in range(len(stop.disciplinas)):
                    if (stop.disciplinas[i][j] == disciplina):
                        if (len(stop.disciplinas[j]) > 2):
                            print("Você já cadastrou duas notas nesta disciplina, caso queira modificar essas notas volte ao menu!\n")
                        else:
                            stop.disciplinas[i].append(nota)
            stop = stop.next

    #def removerNota(self, nota, disciplina, nome):
    #  stop = self.front
    #  while stop != None:
    #    if stop.aluno == nome:
    #      for i in range(len(stop.disciplinas)):
    #        for j in range(len(stop.disciplinas[i])):
    #          if (stop.disciplinas[i][j] == disciplina):
    #              print(stop.disciplinas[i])
    #            
    #    stop = stop.next
    # inicio = front rear = fim

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
        
    
    def __str__(self): #deletar essa função junto com os testes manuais antes de mandar para Allan
        output = ""
        if self.front:
            aux = self.front
            output += ""
            while (aux): 
                output += "[Aluno: {}]\n[Disciplinas e notas: {}]\n".format(aux.aluno, aux.disciplinas)
            
                if(aux.next):
                    output += "\n"
                aux = aux.next
                output += " "
            else:
                output += "[]"
        return output
  
# daqui para baixo, testes manuais de metódos, organizar menu

controleAcademico = List()

controleAcademico.enqueueAluno("Francileudo")
print(controleAcademico)
print()
controleAcademico.enqueueAluno("Tharcio")
print(controleAcademico)
print()
controleAcademico.enqueueAluno("Beto")
print(controleAcademico)
print()
controleAcademico.enqueueAluno("Carla")
print(controleAcademico)
print()
controleAcademico.enqueueAluno("Daniel")
print(controleAcademico)
print()

print(controleAcademico)

controleAcademico.inserirDisciplina("Estrutura de Dados", "Tharcio")
controleAcademico.inserirDisciplina("Lab. de Estrutura de Dados", "Tharcio")
controleAcademico.inserirDisciplina("Informática na Educação", "Tharcio")

print(controleAcademico)
controleAcademico.inserirDisciplina("Estrutura de Dados", "Francileudo")
print(controleAcademico)
controleAcademico.inserirNota(10, "Estrutura de Dados", "Tharcio")
print(controleAcademico)
controleAcademico.inserirNota(5, "Estrutura de Dados", "Tharcio")
print(controleAcademico)
controleAcademico.inserirNota(10, "Estrutura de Dados", "Tharcio")
print(controleAcademico)
print(controleAcademico.visualizarMediaEmDisciplina("Tharcio", "Estrutura de Dados"))
print(controleAcademico.visualizarMediaEmDisciplina("Francileudo", "Estrutura de Dados"))
print(controleAcademico.tamanhoDaLista())

controleAcademico.removerDisciplina("Lab. de Estrutura de Dados", "Francileudo")
controleAcademico.removerDisciplina("Lab. de Estrutura de Dados", "Tharcio")

controleAcademico.removeAluno("Daniel")
print(controleAcademico)
controleAcademico.removeAluno("Beto")

print(controleAcademico)

# daqui para baixo refere-se a código do menu, completando ele à medida que o código fica pronto

choose = -1
continuaMenu = 1

while (continuaMenu != 0):
    print("-" * 50)
    print("Controle Acadêmico")
    print()
    print("1 - Cadastrar aluno\n \n2 - Cadastrar disciplinas\n \n3 - Cadastrar notas em disciplina\n \n4 - Remover aluno\n \n5 - Remover disciplina\n \n6 - Remover nota de disciplina\n \n7 - Atualizar dados do aluno\n \n8 - Atualizar disciplina de aluno\n \n9 - Atualizar nota de disciplina\n \n10 - Visualize a média de um aluno\n \n11 - Visualize quais alunos estão com a média menor que 7\n \n12 - Visualize quais alunos estão com média maior ou igual a 7\n \n13 - Visualize as notas das disciplinas cadastradas em um aluno\n \n")
    print()
    print("-" * 50)
    choose = int(input("Digite um número: "))

    if (choose == 1):

        aluno = input("Digite o nome do aluno: ")
        controleAcademico.enqueueAluno(aluno)
        print("Aluno cadastrado")
        print()

        continuaMenu = int(input("Deseja sair do Programa agora?\nDigite 0 para sim e 1 para não: "))

    elif (choose == 2):

        nomeDisciplina = input("Digite o nome da disciplina: ")
        aluno = input("Digite o nome do aluno cadastrado: ")
        controleAcademico.inserirDisciplina(nomeDisciplina, aluno)
        print()

        continuaMenu = int(input("Deseja sair do Programa agora?\nDigite 0 para sim e 1 para não: "))

    elif (choose == 3):

        disciplina = input("digite o nome da disciplina: ")
        nota = int(input("Digite a nota: "))
        aluno = input("Digite o nome do aluno: ")
        controleAcademico.inserirNota(nota, disciplina, aluno)
        print()

        continuaMenu = int(input("Deseja sair do Programa agora?\nDigite 0 para sim e 1 para não: "))

    elif (choose == 4):
        aluno = input("Digite o nome do aluno: ")
        controleAcademico.removeAluno(aluno)
        print()

        continuaMenu = int(input("Deseja sair do Programa agora?\nDigite 0 para sim e 1 para não: "))
    
    elif (choose == 5):

        disciplina = input("digite o nome da disciplina: ")
        aluno = input("Digite o nome do aluno: ")  
        controleAcademico.removerDisciplina(disciplina , aluno)
        print()

        continuaMenu = int(input("Deseja sair do Programa agora?\nDigite 0 para sim e 1 para não: "))

    elif (choose == 6):
        print("remover nota da disciplina do aluno")
        
        print()

        continuaMenu = int(input("Deseja sair do Programa agora?\nDigite 0 para sim e 1 para não: "))
    
    elif (choose == 7):
        print("Atualizar dados do aluno, no nosso caso o nome dele apenas")
        controleAcademico.buscaAluno(aluno)
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

        print(controleAcademico.visualizarMediaEmDisciplina(aluno, disciplina))
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
        print(controleAcademico.visualizacaoCompletaDeAluno(aluno))
        print()

        continuaMenu = int(input("Deseja sair do Programa agora?\nDigite 0 para sim e 1 para não: "))
    
    else:
        print("Digite um número válido!")

