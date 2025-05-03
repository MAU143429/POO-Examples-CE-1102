class Suma(object):
    def __init__(self):
        pass
    def sumlista(self,matriz1,matriz2):
        if isinstance (matriz1,list) and isinstance (matriz2,list) and len(matriz1)==len(matriz2) and len(matriz1[0])== len(matriz2[0]):
            return self.sumlista_aux(matriz1,matriz2)
        else:
            return "ERROR"
    def sumlista_aux(self,matriz1,matriz2):
        matriznew = []
        resultado = []
        for fila in range(len(matriz1)):
            resultado = []
            for col in range(len(matriz1[0])):
                resultado += [(matriz1[fila][col]) + (matriz2[fila][col])]
            matriznew += [resultado]   
        print(matriznew)
