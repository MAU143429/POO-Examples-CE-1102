def busca_bin_aux(Lista, Ele, Ini, Fin):
    if Fin<Ini:
        return False
    Mitad=(Ini+Fin)//2
    if  Lista[Mitad]>Ele:
        return busca_bin_aux(Lista, Ele, Ini, Mitad-1)
    elif Lista[Mitad]<Ele:
        return busca_bin_aux(Lista, Ele, Mitad+1, Fin)
    else:
        return Mitad



##########################################################
def burbuja(Lista):
    return burbuja_aux(Lista, 0, 0, len(Lista), False)

def burbuja_aux(Lista, i, j, n, Swap):
    if i==n:
        return Lista
    if j==n-i-1:
        if Swap:
            return burbuja_aux(Lista, i+1, 0, n, False)
        else:
            return Lista
    if Lista[j]>Lista[j+1]:
        Tmp=Lista[j]
        Lista[j]=Lista[j+1]
        Lista[j+1]=Tmp
        return burbuja_aux(Lista, i, j+1, n, True)
    else:
        return burbuja_aux(Lista, i, j+1, n, Swap)

#########################################################
def seleccion(Lista):
    return seleccion_aux(Lista, 0, len(Lista))

def seleccion_aux(Lista, i, n):
    if i==n:
        return Lista
    Min=menor(Lista, i+1, n, i)
    Tmp=Lista[i]
    Lista[i]=Lista[Min]
    Lista[Min]=Tmp
    return seleccion_aux(Lista,i+1,n)
def menor(Lista,j,n,Min):
    if j==n:
        return Min
    if Lista[j]<Lista[Min]:
        Min=j
    return menor(Lista,j+1,n,Min)

#########################################################
def insert_sort(Lista):
    return insert_sort_aux(Lista,1,len(Lista))
def insert_sort_aux(Lista,i,n):
    if i==n:
        return Lista
    Aux=Lista[i]
    j=incluye_orden(Lista,i,Aux)
    Lista[j]=Aux
    return insert_sort_aux(Lista,i+1,n)
def incluye_orden(Lista,j,Aux):
    if j<=0 or Lista[j-1]<=Aux:
        return j
    Lista[j]=Lista[j-1]
    return incluye_orden(Lista,j-1,Aux)
