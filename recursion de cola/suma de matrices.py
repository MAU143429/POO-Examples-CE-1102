class matrices(object):
    def __init__(self):
        pass

    def suma(self,matriz1,matriz2):
        if (isinstance(matriz1,list) and isinstance(matriz2,list) and len(matriz1) == len(matriz2) and  len(matriz1[0])==len(matriz2[0])):
            return self.suma_aux(matriz1,matriz2,0,0,[],[])
        else:
            return "ERROR"
    def suma_aux(self,matriz1,matriz2,fila,col,result,fila2):
        if fila == len(matriz1):
            return result
        elif col == len(matriz1[0]):
            return self.suma_aux(matriz1,matriz2,fila+1,0,result+[fila2],[])
        else:
            return self.suma_aux(matriz1,matriz2,fila,col+1,result,fila2+(matriz1[fila][col]+matriz2[fila][col]))
