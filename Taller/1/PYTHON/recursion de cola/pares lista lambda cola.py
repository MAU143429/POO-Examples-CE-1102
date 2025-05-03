class Operacion(object):
        def __init__(self):
            pass

        def pares(self,lista):
            if isinstance (lista,list):
                par = lambda digito:digito %10 % 2 == 0
                return self.pares_aux(lista,par,[])
            else:
                return "ERROR"

        def pares_aux(self,lista,cond,result):
            if lista == []:
                 return result
            elif cond(lista[0]):
                return self.pares_aux(lista[1:],cond,result+[lista[0]])
            else:
                return self.pares_aux(lista[1:],cond,result)
                         
