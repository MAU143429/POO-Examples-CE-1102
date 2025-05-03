class Cola:
    def __init__(self):
        self.__data=[]
        self.__size = 0
        def len(self):
            return self.__size
        def is_empty(self):
            return self.__size == 0
        def first(self):
            if self.is_empty():
                raise Exception ("Vacía")
            return self.__data[0]
        def dequeue(self):
            if self.is_empty():
                raise Exception ("Vacía")
            answer = self.__data[0]
            self.__data = self.__data[1:]
            self.__size -=1
            return answer
        def enqueue(self,e):
            self.__data.append(e)
            self.__size += 1

        def imprimir1(self):
            print(self._data)

        def imprimir2(self):
            self.valorImprimir = ""
            for valor in self._data:
                self.valorImprimir = self.valorImprimir + str(valor) + " "
            return self.valorImprimir
        def __str__(self):
            return self.imprimir2()
        def __len__(self):
            return self.__size
