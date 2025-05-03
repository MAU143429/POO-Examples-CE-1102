def form_par(num):
    if isinstance (num, int):
        return form_par_aux(num, 0)
    else: return "ERROR"

def form_par_aux(num, potencia):
    if num == 0 :
        return 0
    elif num % 10 % 2 == 0:
        return((num % 10) * (10 ** potencia) +
                form_par_aux(num // 10, potencia+1))
    else:return form_par_aux (num // 10, potencia)
