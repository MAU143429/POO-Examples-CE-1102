class Sumatoria:

    def __init__(self):
        pass
    
    def suma(self,lista1,lista2,base,acarreo):
        if isinstance(lista1,list) and isinstance(lista2, list)and isinstance(base, int) and isinstance (acarreo,int) and len(lista1)== len(lista2):
           return self.suma_aux(lista1,lista2,base,acarreo)
        else: return "ERROR LOS PARAMETROS INGRESADOS SON INCORRECTOS"

    def suma_aux (self,lista1,lista2,base,acarreo):
        if lista1 == [] and lista2 == [] and base >= 0 and acarreo >= 0:
           return [acarreo]
        
        elif (lista1[-1] - lista2[-1]+acarreo)== 0:
            return self.suma_aux(lista1[:-1],lista2[:-1],base,0)+([lista1[-1]+lista2[-1]+ acarreo % base])
    
        elif (lista1[-1]-lista2[-1]+acarreo) < base:
            return self.suma_aux(lista1[:-1],lista2[:-1],base,1)+[0]

        else:
            return self.suma_aux (lista1[:-1],lista2[:-1],base,0)+[lista1[-1]+lista2[-1]+acarreo]
       
