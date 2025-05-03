def cant_digitos(lista, longitud):
    if isinstance (lista, int) and isinstance(longitud, int):
        return cant_digitos_aux(lista)
    else:
        return "ERROR"
def cant_digitos_aux(lista, longitud):
    if(Lista == 0):
     return 0

    else:
        return  lista // longitud + cant_digitos_aux(lista // 10)
