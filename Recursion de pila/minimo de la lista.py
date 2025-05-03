def minux(lista):
    if isinstance (lista, list):
        return minimum(lista)
    else:return "ERROR"

def minimum(lista):
    if lista[1:] == []:
        return lista[0]
    elif lista [0] <= lista[1]:
        return minimum([lista[0]]+lista[2:])
    else:
        return minimum(lista[1:])
