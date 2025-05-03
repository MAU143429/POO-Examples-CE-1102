def cant_pares(num):
    if(isinstance(num, int) and (num >0)):

       return cant_pares_aux(num)
    else: return "ERROR"

def cant_pares_aux (num):
    if(num == 0):
        return 0
    elif (num % 10 % 2 == 0):
        return 1 + cant_pares_aux (num // 10)
    else: return cant_pares_aux(num // 10)
