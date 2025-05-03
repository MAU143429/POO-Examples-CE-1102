def eliminar_num(lista, num):
    if isinstance (lista, list):
        return eliminar_num_aux(lista, num)
    else:return "ERROR"

def eliminar_num_aux(lista, num):
    if lista == []:
        return []
    elif lista [0] == num:
        return eliminar_num_aux(lista[1:], num)
    else:
        return [lista[0]]+eliminar_num_aux(lista[1:], num)
