def num_repetido (num,dig):
    if((isinstance(num, int) and (num > 0))
       and (isinstance(dig, int) and (dig >= 0))):

       return num_repetido_aux(num, dig)
    else: return "ERROR"

def num_repetido_aux (num, dig):
       if(num == 0):
        return 0
       elif (num % 10 == dig):
        return 1 + num_repetido_aux(num // 10, dig)
       else: return num_repetido_aux (num // 10, dig)
