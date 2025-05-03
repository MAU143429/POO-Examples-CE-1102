class Operacion(object):
        def __init__(self):
            pass

        def recorrer(self,lista):
            if isinstance (lista,list):
                return self.recorrer_aux(lista,0,0)
            else:
                return "ERROR"

        def recorrer_aux(self,lista,result,indice):
            if indice == len (lista):
                 return result
            else:
                return self.recorrer_aux(lista,result+lista[indice],indice+1)
