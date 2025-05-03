class matrices(object):
    def __init__(self):
        pass

    def cambiar(self,matriz):
        if isinstance(matriz,list):
            return self.cambiar_aux(matriz,0,0)
        else:
            return "ERROR"
    def cambiar_aux(self,matriz,fila,col):
        if fila == len(matriz):
            return matriz
        elif col == len(matriz[0]):
            return self.cambiar_aux(matriz,fila+1,0)
        elif (fila == 0 or fila == (len(matriz)-1) or col == 0 or col ==(len(matriz[0])-1)):
            matriz[fila][col]="*"
            return (self.cambiar_aux(matriz,fila,col+1))
        else: 
            return (self.cambiar_aux(matriz,fila,col+1))
    
