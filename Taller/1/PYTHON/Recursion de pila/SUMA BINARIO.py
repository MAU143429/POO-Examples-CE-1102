def suma_bin(lista1,lista2,acarreo):
    if (isinstance(lista1,list)) and (isinstance(lista2, list))and (isinstance (acarreo, int))and len(lista1) == len(lista2):
        return suma_bin_aux(lista1,lista2,acarreo)

    else:return "ERROR LISTAS INVALIDAS"

    
def suma_bin_aux(lista1,lista2,acarreo):
    if lista1==[] and lista2 ==[]:
     return[]
    elif (0+0==0)and (1+0==1) and (0+1==1) and (1+1==0):
        return ((lista1[0])+(lista2)[0])
        
    
