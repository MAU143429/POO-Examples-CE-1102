def suma_lista(lista):
    if isinstance(lista, list):
        return suma_lista_aux(lista)
    else: return "ERROR NO UNA LISTA"

def suma_lista_aux(lista):
    if lista == []:
        return 0
    else:
        return lista[0] + suma_lista_aux(lista[1:])
