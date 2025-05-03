class Matriz(object):
    def __init__(self):
        pass
    def transponer(self,matriz):
        if isinstance (matriz,list):
            return self.transponer_aux(matriz,0,0,[],[])
        else:
            return "ERROR"
    def transponer_aux(self,matriz,fila,col,result,filaux):
        if col == len(matriz[0]):
            return result
        elif fila ==len(matriz):
            return self.transponer_aux(matriz,0,col+1,result+[filaux],[])
        else:
            return (self.transponer_aux(matriz,fila+1,col,result,filaux + [matriz[fila][col]]))
