def multi(digi,num):
    if isinstance (digi,int) and (num,int):
        return multi_aux(digi,num,0)
    else:
        return"ERROR"

def multi_aux(digi,num,potencia):
    if num == 0:
        return 0
    elif(digi* (num%10))<= 9:
        return digi*(num%10)* 10 ** potencia + multi_aux(digi,num//10,potencia+1)
    else:
        return multi_aux(digi,num//10,potencia)
