import math

def sumatoria(L1):
    if isinstance(L1,list):
        return sumatoria1(L1,len(L1)-1)
    else:"Error"

def sumatoria1(lista,n):
    if(n < 0):
        return 0
    else:
        return  math.sqrt(lista[n])+sumatoria1(lista,n-1)

