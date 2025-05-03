def sumalista(lista1, lista2):
    if (isinstance(lista1, list) and isinstance(lista2, list)
        and len(lista1)== len(lista2)):
        return sumalista_aux (lista1, lista2)
    else:return "ERROR DE VALIDACIÓN"

def sumalista_aux (lista1, lista2):
    if lista1 == [] and lista2 == []:
        return[]
    else: return([lista1[0] + lista2[0]])+ sumalistas_aux (lista1 [1:], lista2[1:])
