class Suma(object):
    def __init__(self):
        pass
    def diagonal(self,matriz):
        if isinstance (matriz,list):
            return self.diagonal_aux(matriz)
        else:
            return "ERROR"
    def diagonal_aux(self,matriz):
        anti_diagonal = []
        for fila in range(len(matriz)):
            
            for fila in range(filas):
                anti_diagonal += [matriz1[fila][-(fila+1)]]
            
               
        print(anti_diagonal)
