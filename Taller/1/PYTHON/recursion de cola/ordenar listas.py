class Ordenar (object):
    def __init__(self):
        pass
    def orden(self,lista):
        if isinstance(lista,list):
            return self.orden_aux(lista,0)
        else:
            return"ERROR"
    def orden_aux(self,lista,indice):
            if indice == len(lista)-1:
              return lista
            else:
                return self.orden_aux(self.orden2_aux((lista,0),indice+1))
            
    def orden2_aux(self,lista,indice):
        if indice == len(lista)-1:
          return lista
        elif lista[indice] > lista[indice+1]:
            aux=lista[indice]
            lista[indice]==lista[indice+1]
            lista[indice+1]==aux
            return self.orden2_aux(lista,indice+1)
        else: return self.orden2_aux(lista,indice+1)
        
   

   
