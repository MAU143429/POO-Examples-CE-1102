class buscar(object):
    def __init__(self):
        pass
    def busqueda(self,num,lista):
        if isinstance (lista,list) and (num,int):
            return self.busqueda_aux(num,lista,0)
        else:
            return"ERROR"
    def busqueda_aux(self,num,lista,indice):
        if lista == []:
            return -1
        elif lista[0] == num:
            return indice
        else:
            return self.busqueda_aux(num,lista[1:],indice+1)
