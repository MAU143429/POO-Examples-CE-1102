class promedio:
    def __init__(self):
        pass
    def prom(self,lista1):
        if isinstance (lista1, list) and len(lista1)>0:
            return self.prom_aux((lista1)**(1/len(lista1))+ self.prom_aux(lista1))
        else:
            return "ERROR EN LA LISTA"
    def prom_aux(self,lista1):
        if lista1 == []:
            return 0
        else:
            return lista1[0]*self.prom_aux(lista1[1:])

