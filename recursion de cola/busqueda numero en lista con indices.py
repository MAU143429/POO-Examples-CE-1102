class buscar(object):
    def __init__(self):
        pass
    def busqueda(self,num,lista):
        if isinstance (lista,list) and isinstance(num,int):
            return self.busqueda_aux(num,lista,0,[])
        else:
            return"ERROR"
    def busqueda_aux(self,num,lista,indice,resultado):
        if indice == len(lista):
            return resultado
        elif lista[indice] == num:
            return self.busqueda_aux(num,lista,indice+1,resultado+[indice])
        else:
            return self.busqueda_aux(num,lista,indice+1,resultado)
