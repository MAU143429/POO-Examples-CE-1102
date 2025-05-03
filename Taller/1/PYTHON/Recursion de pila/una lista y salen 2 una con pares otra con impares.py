def pares_impares(lista):
    if isinstance(lista, list):
        pares=lambda digito: digito % 2 == 0
        impares=lambda digito: digito % 2 == 1
        return (pares_impares_aux(lista, pares), pares_impares_aux(lista, impares))
    else:
        return "ERROR NO ES UNA LISTA"

def pares_impares_aux(lista, condicion):
    if (lista) == []:
        return []

    elif condicion(lista[0]):
        return [lista[0]]+ pares_impares_aux(lista[1:], condicion)

    else:
        return pares_impares_aux(lista[1:], condicion)
