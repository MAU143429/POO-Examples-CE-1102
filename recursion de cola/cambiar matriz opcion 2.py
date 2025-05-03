class matriz(object):
    def __init__(self):
        pass
    def crearMatriz(self,n):
        if isinstance(n,int) and n>0:
            return self.crearMatriz_aux(n,[],[],0,0)
        else:
            return "ERROR"
    def crearMatriz_aux(self,n,matriz,fila,indiceFila,indiceColumna):
        if indiceFila == n:
            return matriz
        elif indiceColumna == n:
            return(self.crearMatriz_aux(n,matriz+[fila],[],indiceFila + 1,0))
        elif indiceFila == 0 or indiceFila == (n-1):
            return(self.crearMatriz_aux(n,matriz,fila+["*"],indiceFila,indiceColumna + 1))
        elif indiceColumna == 0 or indiceColumna == (n-1):
            return(self.crearMatriz_aux(n,matriz,fila+["*"],indiceFila,indiceColumna + 1))
        else:
            return (self.crearMatriz_aux(n,matriz,fila+[0],indiceFila,indiceColumna+1))
