#Recursion de Cola

#1 cola
def mayor (num):
    if isinstance (num,int):
        return mayor_aux(num,0)
    else:
        return "ERROR"
def mayor_aux(num,mayor):
    if num == 0:
        return mayor
    if num%10 > mayor:
       return mayor_aux(num//10,mayor=num%10)
    else:
        return mayor_aux(num//10,mayor)
#1 pila
def mayor_pila (num):
    if isinstance (num,int):
        return mayor_pila_aux(num)
    else:
        return "ERROR"
def mayor_pila_aux(num):
    if num == 0:
        return 0
    if num%10 > num%100 :
       return num %10 + mayor_pila_aux(num//10)
    else:
        return num%100 + mayor_pila_aux(num//10)

#2 cola
def restar(num,dig):
    if isinstance(num,int) and isinstance(dig,int):
        return restar_aux(num,dig,0,1)
    else:
        return "ERROR"
def restar_aux(num,dig,result,potencia):
    if num == 0:
        return int(result//10)
    else:
        return restar_aux(num//10,dig,result+((((num%10)-dig)*(10**potencia))),potencia+1)
#3 cola
def cambia(num):
    if isinstance (num,int):
        return cambia_aux(num,0,1)
    else:
        return "ERROR"
def cambia_aux(num,result,potencia):
    if num%10 == 0:
        return int(result/10)
    if (num%10)%4 == 0:
        return cambia_aux(num//10,result,potencia+1)
    else:
        return cambia_aux(num//10,result+((num%10)*(10**potencia)),potencia+1)
#4 cola
def hay_div(num,dig):
    if isinstance(num,int) and isinstance(dig,int):
        return hay_div_aux(num,dig)
    else:
        return "ERROR"
def hay_div_aux(num,dig):
    if num == 0:
        return False
    if (num%10)%dig == 0:
        return True
    else:
        return hay_div_aux(num//10,dig)

#5 cola
def hay_div(num,dig):
    if isinstance(num,int) and isinstance(dig,int):
        return hay_div_aux(num,dig)
    else:
        return "ERROR"
def hay_div_aux(num,dig):
    if num == 0:
        return True
    if (num%10)%dig == 0:
        return False
    else:
        return hay_div_aux(num//10,dig)
        
