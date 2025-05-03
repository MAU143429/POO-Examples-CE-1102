def sumatoria(L1):
    if isinstance(L1,list):
        return sumatoria1(L1,len(L1)-1),sumatoria2(L1)
    else:"Error"

def sumatoria1(lista,n):
    if(n==0):
        return 0
    else:
        return (lista[n]*n*5**3)+sumatoria1(lista,n-1)

def sumatoria2(lista):
    if(lista== []):
        return 0
    else:
        return((lista[-1]*(len(lista)-1)*5**3)+ sumatoria2(lista[:-1]))
