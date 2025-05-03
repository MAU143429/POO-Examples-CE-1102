def numeros_positivos(lista):
    if isinstance (lista, list):
        return numeros_positivos_aux(lista)
    else:return "ERROR"

def numeros_positivos_aux(lista):
    if lista == []:
        return "TRUE"
    elif lista [0]<0:
        return "FALSE"
    else:
        return numeros_positivos_aux(lista[1:])
