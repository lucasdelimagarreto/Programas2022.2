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

    def __str__(self):
        output = ""

        if self.frente:
            aux = self.frente

        else:
            return "Não há disciplinas cadastradas para esse aluno"

        while(aux != None):
            output += "\n {}:\nNota 1: {} \nNota 2: {}".format(aux.nomeDisc, aux.nota1, aux.nota2)
            aux = aux.proximo

        return output

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

    def buscaDisciplina(self, nome, disciplina):

        aluno = controleAcademico.buscaAluno(nome)
        aux = aluno.aluno.listaDisciplinas.frente

        while(aux != None):
            if (aux.nomeDisc == disciplina):
                return aux
            aux = aux.proximo

    def inserirDisciplina(self, nome):

        aux = controleAcademico.buscaAluno(nome)
        aux.aluno.listaDisciplinas.enqueueDisciplina()

    def removerDisciplina(self, nome, disciplina):

        aux = controleAcademico.buscaAluno(nome)
        stop = aux.aluno.listaDisciplinas
        count = 0

        while (stop != None):
            if (stop.nomeDisc == disciplina):

                stop.disciplina.pop(count)
                print("Aluno removido com sucesso da disciplina")
                return

            count += 1
            stop = stop.diciplina.proximo

        print("Esse aluno não está matriculado nessa disciplina, logo não pode ser removido dela")

    def inserirNota(self):

        var = controleAcademico.buscaDisciplina(pedeInfo(1), pedeInfo(2))
        aux = True

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

        temp = controleAcademico.buscaDisciplina(pedeInfo(1), pedeInfo(2))
        aux = True

        if (temp.nota1 == None and temp.nota2 == None):
            print("Voce ja removeu as notas deste aluno!\n")

        else:
            while(aux):
                nota = int(input("Qual nota deseja remover 1a ou 2a:"))

                if(nota == 1):
                    temp.nota1 = None
                    if(temp.nota1 == None):
                        print("A nota foi definida para: ", temp.nota1)
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
            anterior = aux
            aux = aux.next
            #aux.anterior.next = aux.next
            #aux.next.anterior = aux.anterior

            if aux:
                anterior.next = aux.next

            else:
                anterior.next = None

        self.__tamanho -= 1

    #def rear(self):
    #   return self.rear

    def visualizarMediaEmDisciplina(self, nome, disciplina):
        aux = controleAcademico.buscaDisciplina(nome, disciplina)
        media = (aux.nota1 + aux.nota2) / 2
        return media

    def visualizacaoCompletaDeAluno(self, aluno):
        if self.front:
            aux = self.front

            while (aux):
                if (aux.aluno.nomeAluno == aluno):
                    output = "Aluno: {}\nDisciplinas e notas: {}\n".format(aux.aluno.nomeAluno, aux.aluno.listaDisciplinas)
                    return output

                aux = aux.next

            return "O Aluno não está cadastrado no controle acadêmico ou você digitou o nome dele errado!"

    def alunosReprovados(self, disciplina):
        output = "Reprovados em {}:\n".format(disciplina)
        if self.front:
            aux = self.front

            while (aux):
                if (self.visualizarMediaEmDisciplina(aux.aluno.nomeAluno, disciplina) < 7.0):
                    output += "{}\n".format(aux.aluno.nomeAluno)
                    return output

                aux = aux.next

    def alunosAprovados(self, disciplina):
        output = "Aprovados em {}:\n".format(disciplina)

        if self.front:
            aux = self.front

            while (aux):
                if (self.visualizarMediaEmDisciplina(aux.aluno.nomeAluno, disciplina) >= 7.0):
                    output += "{}\n".format(aux.aluno.nomeAluno)
                    return output

                aux = aux.next

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

    if (choose == 1): #FUNCIONA ok
        # 1 - Cadastrar aluno
        controleAcademico.enqueueAluno(pedeInfo(1))
        #print("Aluno de nome",controleAcademico.front.aluno.nomeAluno, " cadastrado")
        print()

    elif (choose == 2): #FUNCIONA ok
        # 2 - Cadastrar disciplinas

        aux = controleAcademico.inserirDisciplina(pedeInfo(1))
        print("A disciplina inserida foi: ", aux)
        print()

    elif (choose == 3): #FUNCIONA ok
        # 3 - Cadastrar notas em disciplina
        print("Cadastrar notas!")
        controleAcademico.inserirNota()
        print()

    elif (choose == 4):
        # 4 - Remover aluno
        #print("Cadastrar notas!")
        controleAcademico.removeAluno(pedeInfo(1))
        print()

    elif (choose == 5):
        # 5 - Remover disciplina

        controleAcademico.removerDisciplina(pedeInfo(1), pedeInfo(2))
        print()

    elif (choose == 6): #FUNCIONA ok
        # 6 - Remover nota de disciplina

        print("remover nota da disciplina do aluno")
        controleAcademico.removerNota()
        print()

    elif (choose == 7): #FUNCIONA ok
        # 7 - Atualizar dados do aluno

        print("Atualizar dados do aluno, no nosso caso o nome dele apenas")
        controleAcademico.buscaAluno(pedeInfo(1))
        novoNome = input("Digite o novo nome do aluno: ")
        controleAcademico.front.aluno.nomeAluno = novoNome
        print(f"Nome do aluno corrigido para {novoNome}")
        print()

    elif (choose == 8): #FUNCIONA ok
        # 8 - Atualizar disciplina de aluno

        print("Atualizar disciplina do aluno.(no caso o nome da disciplina)")
        disciplina = controleAcademico.buscaDisciplina()
        disciplina.nomeDisc = input("Digite o nome da disciplina corrigido: ")
        print("O nome da disciplina foi alterado para: ", disciplina.nomeDisc)
        print()

    elif (choose == 9): #funciona ok
        # 9 - Atualizar nota de disciplina

        print("Atualizar nota de disciplina de aluno")
        controleAcademico.inserirNota()

        print()

    elif (choose == 10): #funcionando ok

        print("A média é: ", controleAcademico.visualizarMediaEmDisciplina(pedeInfo(1), pedeInfo(2)))
        print()

    elif (choose == 11): #funcionando ok
        print(controleAcademico.alunosReprovados(pedeInfo(2)))
        print()

    elif (choose == 12): #funcionando ok
        print(controleAcademico.alunosAprovados(pedeInfo(2)))
        print()

    elif (choose == 13): #funcionando ok

        print(controleAcademico.visualizacaoCompletaDeAluno(pedeInfo(1)))
        print()

    else:
        print("Digite um número válido!")

    continuaMenu = int(input("Deseja sair do Programa agora?\nDigite 0 para sim e 1 para não: "))
