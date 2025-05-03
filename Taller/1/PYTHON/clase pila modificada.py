class Pila:
    def __init__(self):
        self.__pi = [ ]
    def len(self):
        return len(self.__pi)
    def is_empty(self):
        return len(self.__pi) == 0
    def push(self,e):
        self.__pi.append(e)
    def top(self):
        if self.is_empty():
            raise MiGatito("Stack is empty")
        else: return self.__pi[-1]
    def pop(self):
        if self.is_empty():
            raise MiGatito("Stack is empty")
        else: return self.__pi.pop()
    def test(self):
        try:
            self.stack = Pila()
            self.stack.push(5)
            self.stack.push(8)
            self.stack.push(4)
            self.stack.push(1)
            self.stack.push(9)
            self.stack.push(5)
            self.stack.push(7)
            print("Numero de elementos en la pila:",self.stack.len())
            print("Elemento en la parte superior de la pila:",self.stack.top())
            while  self.stack.is_empty() == False:
                 print("Saca elemento :",self.stack.pop())
            x=5
            y=0
            c= x/y
        except MiGatito as e:
            print("Ocurrió un error al sacar un elemento de una pila vacia:",str(type(e)),e.message)
        except ZeroDivisionError as d:
            print("Ocurrió un error al dividir.")
        else:
            print("Resultado")
        finally:
            print("Finally")
class MiGatito(Exception):
    def __init__(self,message):
        self.message = message

class DivisionCero(ZeroDivisionError):
    def __init__(self,message):
        self.message = message
            
        
            
