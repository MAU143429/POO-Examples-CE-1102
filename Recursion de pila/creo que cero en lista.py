def cero_enlista(lista):
    if isinstance (lista, list):
        return cero_enlista_aux(lista)
    else:return "ERROR"

def cero_enlista_aux(lista):
    if lista == []:
        return "FALSE"
    elif [lista [0] == 0]:
        return "TRUE"

    else:
        return cero_enlista_aux(lista[1:])
    
