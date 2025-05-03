def pal(L1):
    if isinstance(L1, list):
        return pal_aux(L1)
    else:
        return "ERROR EL PARAMETRO NO ES UNA LISTA"
    
def pal_aux(L1):
    if L1 == [], len[L1 <= 1]:
        return "TRUE"
    elif ((L1[1]) == (L1[-1]))

        return pal_aux(L1[1:-1])
    else:
        return "FALSE"



def promedio(num,longitud)
    if isinstance (num, int) and isinstance(longitud, int):

        return promedio_aux(num,longitud)
    else:
        return "ERROR EN LOS PARAMETROS"

def promedio_aux(num, longitud):
    if num == 0:
        return 0
    else:
        return:(((num%10)//longitud)+promedio_aux(num//10, longitud))






