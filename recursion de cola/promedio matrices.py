class matrices(object):
    def __init__(self):
        pass

    def suma(self,matriz):
        if isinstance(matriz,list):
            return self.suma_aux(matriz,0,0,0)
        else:
            return "ERROR"
    def suma_aux(self,matriz,fila,col,result):
        if fila == len(matriz):
            return result/(len(matriz)*len(matriz[0]))
        elif col == len(matriz[0]):
            return self.suma_aux(matriz,fila+1,0,result)
        else:
            return self.suma_aux(matriz,fila,col+1,result+matriz[fila][col])

