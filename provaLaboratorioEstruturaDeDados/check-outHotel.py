class Cliente():
    
    def __init__(self, nome, sexo, cpf, gastos, estadia, estadoEstadia):
        self.__nome = nome
        self.__sexo = sexo
        self.__cpf = cpf
        self.__gastos = gastos
        self.__estadia = estadia
        self.__estadoEstadia = estadoEstadia

    
    def cadastraCliente(self):
        self.__nome = input("Digite o nome do cliente: ")
        self.__sexo = input("Digite a opção sexual do cliente: ")
        self.__cpf = int(input("Digite o cpf do cliente: "))
        self.__estadia = float(input("Digite o quantos dia o cliente permaneceu no hotel: "))
        self.__gastos = float(input("Digite o quanto o cliente gastou na estadia: "))
        self.__estadoEstadia = True

    


    def get_nome(self):
        return self.__nome
    
    def set_nome(self, nome):
        self.__nome = nome

    def get_sexo(self):
        return self.__sexo

    def set_sexo(self, sexo):
        self.__sexo = sexo

    def get_cpf(self):
        return self.__cpf
    
    def set_cpf(self, cpf):
        self.__cpf = cpf

    def get_estadia(self):
        return self.__estadia

    def set_estadia(self, estadia):
        self.__estadia = estadia
    
    def get_gastos(self):
        return self.__gastos

    def set_gastos(self, gastos):
        self.__gastos = gastos

    def get_estadoEstadia(self):
        return self.__estadoEstadia

    def set_estadoEstadia(self, estadoEstadia):
        self.__estadoEstadia = estadoEstadia

class Node:

    def __init__(self, valor):
        self.valor = valor
        self.proximo = None


class LinkedList:

    def __init__(self):
        self.head = None

    def insere_inicio(self, elemento):
        elemento.proximo = self.head
        self.head = elemento

    def insere_final(self, elemento):
        novo_no = elemento
        if self.head is None:
            self.head = novo_no
            return
        temp = self.head
        while temp.proximo != None:
            temp = temp.proximo
        temp.proximo = novo_no

    def inserePorPosicao(self, elemento, posicao):
        pass


    def remove2(self, valor):
      current = self.head
      previous = None
      found = False
      while not found:
          if current.valor == valor:
              found = True
          else:
              previous = current
              current = current.proximo
      if previous == None:
          self.head = current.proximo
      else:
          previous.proximo = current.proximo
  
    def remove1(self, valor):
        temp = self.head
        if (temp != None):
            if (temp.valor == valor):
                self.head = temp.proximo
                temp = None
                return
        while(temp != None):
            if temp.valor == valor:
                break
            prev = temp
            temp = temp.proximo
        if(temp == None):
            return
        prev.proximo = temp.proximo
        temp = None

    def pesquisa(self, valor):
        current = self.head
        encontrou = False
        while current != None and not encontrou:
            if current.valor == valor:
                encontrou = True
                return encontrou
            else:
                current = current.proximo
        return encontrou

    def pesquisaRetornaPosicao(self, valor):
        current = self.head
        posicao = 0
        while current != None:
            if current.valor == valor:
                posicao += 1
                return posicao
            else:
                current = current.proximo
                posicao += 1
        return posicao

    def tamanho(self):
        count = 0
        temp = self.head
        while(temp != None):
            count = count + 1
            temp = temp.proximo
        return count

    def imprimeSequencia(self):
        node = self.head
        nodes = []
        while node is not None:
            nodes.append(node.valor)
            node = node.proximo
        nodes.append('NULL')
        values = ' -> '.join(str(v) for v in nodes)
        return values

    def valorMinino(self):
        min = 32767
        while self.head != None:
            if min > self.head.valor:
                min = self.head.valor
            self.head = self.head.proximo
        return min

    def valorMaximo(self):
        max = self.head.valor
        atual = self.head
        while atual.proximo != None:
          if atual.valor > max:
            max = atual.valor
          atual = atual.proximo
        return max 

minhaLinked = LinkedList()
clientes = Cliente()

numClientes = int(input("Digite o numero de clientes: "))

for i in range(numClientes):
    minhaLinked.insere_final(Node(clientes.cadastraCliente))

