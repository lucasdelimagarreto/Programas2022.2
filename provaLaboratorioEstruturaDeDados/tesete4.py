class Cliente:
 
  def init(self, cpf, nome, contaBancaria):
    self.cpf = cpf
    self.nome = nome
    self.contaBancaria = contaBancaria
    self.next = None
 
 
class Queue:
 
  def init(self):
    self.front = None
    self.rear = None
 
  def enqueue(self,cpf,nome,contaBancaria):

    cliente1 = Cliente(cpf, nome, contaBancaria)

    if self.front == None:
      self.front = cliente1
      self.rear = cliente1
    else:
      self.rear.next = cliente1
      self.rear = cliente1
 
  def dequeue(self):
    if self.front.cpf == self.rear.cpf:
      self.front = None
      self.rear = None
    self.front = self.front.next
 
minhaQueue = Queue()
minhaQueue.enqueue(int(234558),'ana',int(23454))