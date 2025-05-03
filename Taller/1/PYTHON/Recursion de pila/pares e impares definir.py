def pares_impares (num):
    if isinstance(num, int) and num > 0:
        return pares(num), impares(num)
    else:return "ERROR"

def pares(num):
    if num == 0:
        return 0
    elif ((num % 10) % 2 == 0):
          return 1 + pares (num // 10)
    else:
         return pares(num // 10)

def impares(num):
    if num == 0 :
      return 0
    elif num % 10 % 2 == 1:
          return 1 + impares(num // 10)
    else:
          return impares(num // 10)
