class Matriz(object):
    def __init__(self):
        pass
    def dia_matriz(self,matriz):
        if isinstance(matriz,list):
            return self.dia_matriz_aux(matriz,0,0)
        else:
            return "ERROR"
    def dia_matriz_aux(self,matriz,indice,result):
        if indice == len(matriz):
            return result
        else:
            return self.dia_matriz_aux(matriz,indice+1,result+matriz[indice][indice])

    
