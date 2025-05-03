class Suma(object):
    def __init__(self):
        pass
    def sumlista(self,L1,L2):
        if isinstance (L1,list) and isinstance (L2,list) and len(L1)==len(L2):
            return self.sumlista_aux(L1,L2)
        else:
            return "ERROR"
    def sumlista_aux(self,L1,L2):
        resultado = 0
        for indice in range(len(L1)):
            resultado += L1[indice] + L2[indice]
        print(resultado)
        
        
