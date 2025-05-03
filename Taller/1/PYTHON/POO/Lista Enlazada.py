class ListaEnlazada:
    #Construye una lista vacia
    def __init__(self):
        self.__head = None
        self.__size = 0
    #Rgeresa el numero de los elementos de la lista
    def __len__(self):
        return self.size
    #determina si un item se encuentra en la lista.
    def contains(self,target):
        curNode = self.__head
        while curNode is not None and curNode.item != target:
            curNode = curNode.net
        if curNode is not None:
             return True
        else:
             return Flase
    #Agrega un nuevo item a la lista
    def add(self,item):
        newNode = Node(item)
        newNode.next = self.__head
        self.__head = newNode
        self.__size += 1
    #Borra un item de la lista
    def remove(self,item):
        predNode = None
        curNode = self.__head
        while curNode is not None and curNode.item != item:
            predNode = curNode
            curNode = curNode.next
        assert curNode is not None, "EL ITEM DEBE ENCONTRARSE EN LA LISTA"
    #Desenlaza el nodo y regresar el item
        self.__size -= 1
        if curNode is self.__head:
            self.__head = curNode.next
        else:
            predNode.next = curNode.next
        return curNode.item
    def test(self):
        self.add(1)
        self.add(5)
        self.add(6)
        iter = Iterator(self.__head)
        while iter.next() == True
            print("Elemento: ", iter.getNext())
class Node:
    def __init__(self,item):
        self.item = item
        self.next = None
class Iterator:
    def __init__(self,listHead):
        self.curNode = listHead
    def __iter__(self):
        return self
    def next(self):
        if self.curNode is None:
            return False
        else:
            return True
    def getNext(self):
        if self._curNode is None:
            return None
        else:
            item = self._curNode.item
            self._curNode = self._curNode.next
            return item
