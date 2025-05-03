class operacion(object):
    def __init__(self):
        pass
    def bus_bin(self,num,lista):
        if isinstance(num,int) and isisntance(lista,list):
            return self.bus_bin_aux(num,lista,0,len(lista))
        else:
            return "ERROR"

    def bus_bin_aux(self,num,lista,indice,n):
        if indice == len(lista):
            return
    
        elif lista[indice] == num:
                    return self.busqueda_aux(num,lista,indice+1,resultado+[indice])
                else:
                    return self.busqueda_aux(num,lista,indice+1,resultado)

