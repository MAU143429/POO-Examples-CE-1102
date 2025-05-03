def posneg(lista):
    if isinstance(lista, list):
        positivos=lambda digito: digito >= 0
        negativos=lambda digito: digito < 0
        return (posneg_aux(lista, positivos), posneg_aux(lista, negativos))
    else:
        return "ERROR NO ES UNA LISTA"

def posneg_aux(lista, condicion):
    if (lista) == []:
        return []

    elif condicion(lista[0]):
        return [lista[0]]+ posneg_aux(lista[1:], condicion)

    else:
        return posneg_aux(lista[1:], condicion)
