class matrices(object):
    def __init__(self):
        pass

    def suma(self,matriz):
        if isinstance(matriz,list):
            return self.suma_aux(matriz,0)/len(matriz)*len(matriz[0])
        else:
            return "ERROR"
    def suma_aux(self,matriz,result):
        if matriz == []:
            return result
        elif (isinstance(matriz[0],list)):
            return self.suma_aux(matriz[0]+matriz[1:],result)
        else:
            return self.suma_aux(matriz[1:],result+matriz[0])
