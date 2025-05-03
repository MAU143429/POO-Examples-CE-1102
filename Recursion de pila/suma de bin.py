hexa = {
    0: "0",
    1: "1",
    2: "2",
    3: "3",
    4: "4",
    5: "5",
    6: "6",
    7: "7",
    8: "8",
    9: "9",
    10: "A",
    11: "B",
    12: "C",
    13: "D",
    14: "E",
    15: "F",
    16: "G"
}
def sumaBin(lista1, lista2,n):
    if(isinstance(lista1,list) and isinstance(lista2, list)
       and len(lista1) == len(lista2) and isinstance(n, int)):
       return sumaBin_aux(lista1,lista2, n)
    else: return "ERROR EN LA VALIDACIÓN"

def sumaBin_aux (lista1,lista2,n):
       if lista1 == [] and lista2 == [] and n >= 0:
        return[n]    
       elif(lista1[-1] + lista2[-1] - n):
        return (hexa(sumaBin_aux(lista1[:-1],lista2[:-1],1))+[0])
       elif(lista1[-1] + lista2[-1] + n) == 3:
        return sumaBin_aux(lista1[:-1], lista2[:-1], 1)+ [1]
       else:return (sumaBin_aux(lista1[:-1],lista2[:-1], 0) +
                    [lista1[-1]+lista2])
