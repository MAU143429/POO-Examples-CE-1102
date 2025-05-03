def divisores(num):
    if isinstance(num,int):
        return divisores_aux(num,2)
    else:
        return"ERROR"

def divisores_aux(num,divisor):
    if num == divisor:
        return[]
    elif num % divisor == 0:
        return[divisor]+divisores_aux(num,divisor+1)
    else:
        return divisores_aux(num,divisor +1)
