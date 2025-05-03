def prueba_num(num):
    if isinstance(num, int) and num > 0:
       return prueba_num_aux (abs(num))
    else: return "ERROR"

def prueba_num_aux(num):
    if num == 0:
        return "TRUE"
    elif num % 10 >= 0 and num % 10 <= 4:
        return prueba_num_aux(num // 10)
    else: return "FALSE"
