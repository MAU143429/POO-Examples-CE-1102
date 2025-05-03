class Matriz(object):
    def __init__(self):
        pass
    def dia_matriz(self,matriz):
        if isinstance(matriz,list) and len(matriz)==len(matriz[0]):
            return self.dia_matriz_aux(matriz,0,len(matriz)-1,0)
        else:
            return "ERROR"
    def dia_matriz_aux(self,matriz,fila,col,result):
        if fila == len(matriz):
            return result
        else:
            return self.dia_matriz_aux(matriz,fila+1,col-1,result+matriz[fila][col])


#-------------------------------------------------------------------------------------------------------Forma 2


    def dia_matriz2(self,matriz):
        if isinstance(matriz,list) and len(matriz)==len(matriz[0]):
            return self.dia_matriz_aux2(matriz,len(matriz),0,0)
        else:
            return "ERROR"
    def dia_matriz_aux2(self,matriz,largo,fila,result):
         if fila == largo:
            return result
         else:
            return self.dia_matriz_aux2(matriz,largo,fila+1,result+matriz[fila][-(fila+1)])
