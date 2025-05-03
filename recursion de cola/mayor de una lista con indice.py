class Operacion(object):
        def __init__(self):
            pass

        def mayor(self,lista):
            if isinstance (lista,list):
                return self.mayor_aux(lista,0,0)
            else:
                return "ERROR"

        def mayor_aux(self,lista,result,indice):
            if indice == len(lista):
                 return result
            elif lista[indice] >= result:
                return self.mayor_aux(lista,lista[indice],indice+1)
            else: return self.mayor_aux(lista,result,indice+1)
