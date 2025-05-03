def decimal_fracciones(num):
    if isinstance(num,float):
        return (decimal_binario_aux(int(num)),
        fraccion_binario_aux(num - int(num)))

    else: return "El valor no es un real"

def decimal_binario_aux(decimal):
    if decimal == 0:
        return []
    else:return decimal_binario_aux(decimal // 2 ) + [decimal % 2]

def fraccion_binario_aux(fraccion):
    if fraccion == 0.0:
        return []
    else: return ([int(fraccion*2)]+fraccion_binario_aux((fraccion* 2)-int(fraccion*2)))
