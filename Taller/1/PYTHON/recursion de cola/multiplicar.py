def multi(lista):
    if isinstance(lista, list):
        return multi_aux(lista,1)
    else:
           return "ERROR EL VALOR INGRESADO NO ES UNA LISTA"

def multi_aux(lista,result):

    if lista == []:
        return result
    else:return multi_aux(lista[1:],result*lista[0])

    

    
