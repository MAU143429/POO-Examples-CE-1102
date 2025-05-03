class Matriz (object):
    def __init__(self):
        pass
    def matriz_suma(self,lista):
        if isinstance(lista,list):
            return self.recorrer_aux(lista,0,0)
        else:
            return "ERROR"


    def recorrer_aux(self,lista,result,indice):
        if indice == len(lista):
                return result
        elif isinstance(lista[indice],list):
             return (self.recorrer_aux(lista[indice],0,0) + self.recorrer_aux(lista,result,indice+1))
        else:
             return self.recorrer_aux(lista,result+lista[indice],indice+1)

