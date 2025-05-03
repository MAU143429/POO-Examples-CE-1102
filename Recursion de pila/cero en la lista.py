def cero_lista(lista):
    if isinstance(lista, list):
        return cero_lista_aux(lista)
    else:return "ERROR NO ES UNA LISTA"

def cero_lista_aux(lista):
    if lista == []:
     return "FALSE"
    elif lista[0] == 0:
        return "TRUE"
    else: return cero_lista_aux(lista[1:])
