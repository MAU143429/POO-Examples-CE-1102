class Nodo:
      def __init__(self,valor):
            self.next = None
            self.prev = None
            self.valor = valor

      def get_valor(self):
            return self.valor
      
      def set_valor(self,valor):
            self.valor = valor
            
class ListaDoble:
      def __init__(self):
            self.head = None
            self.tail = None
            self.largo = 0
      def appe(self,valor):
            self.largo+=1
            if self.head == None:
                  self.head = Nodo(valor)
                  self.tail = self.head
            else:
                  temp = self.tail
                  ant = temp
                  n1 = Nodo(valor)
                  temp.next = n1
                  x.prev = ant
                  self.tail = n1                       
      def printL(self):
            tmp =self.head
            while tmp != None:
               print(tmp.get_valor())
               tmp = tmp.next
      def rprintL(self):
            tmp = self.tail
            while tmp != None:
                print(tmp.get_valor())
                tmp = temp.prev
      def suma (self):
          nodo = self.head
          sumatoria = 0
          while nodo != None:
                sumatoria += nodo.get_valor()
                nodo = nodo.next
      def dele (self,i):
          k = 0
          temp = self.head
          while temp != None:
                if k == i:
                      ant = temp.prev
                      ant.next = temp.next
                      temp = temp.next
                      temp.prev = ant
                      self.largo -= 1
                      break
                else:
                      k += 1
                      temp = temp.next
      def multi (self, valor):
        temp = self.head
        while temp != None:
            temp.set_valor(temp.get_valor()*valor)
            temp = temp.next
            
      def index (self):
        result = 0
        j = 0
        temp = self.tail
        while temp != None:
            result = temp.get_valor()*10**j
            temp = temp.prev
            j += 1
        return result
