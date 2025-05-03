class Suma(object):
    def __init__(self):
        pass
    def traspuesta(self,matriz):
        if isinstance (matriz,list):
            filas = len(matriz)
            columnas = len(matriz[0])
            return self.sumlista_aux(matriz)
        else:
            return "ERROR"
    def traspuesta_aux(self,matriz,filas,columnas):
        traspuesta = []
        for col in range(columnas):
            filaTraspuesta = []
            for fila in range(filas):
                filaTranspuesta += [matriz1[fila][col]]
            traspuesta += [filaTraspuesta]
               
        print(traspuesta)
