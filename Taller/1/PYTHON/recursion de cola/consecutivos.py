class Operacion(object):
    def __init__(self):
        pass
    def consecu(self,matriz):
        if isinstance(matriz,list) and (len(matriz) == len(matriz[0])):
            return self.consecu_aux(matriz,1)
        else:
            return "ERROR"
    def consecu_aux(self,matriz,contador):
        if contador > (len(matriz)*len(matriz[0])):
            return True
        elif (self.buscar(matriz,contador,0,0)):
            return self.consecu_aux(matriz, contador+1)
        else:
            return False
        
    def buscar(self,matriz,elem,fila,col):
        if fila == len(matriz):
            return False
        elif col == len(matriz[0]):
            return self.buscar(matriz,elem,fila+1,0)
        elif elem == matriz[fila][col]:
            return True
        else:
            return self.buscar(matriz,elem,fila,col+1)
