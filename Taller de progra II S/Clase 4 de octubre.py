1#1#############################################
def digitos(num):
      if isinstance (num,int):
            return digitos_aux(abs(num),0,0)
      else:
            return "ERROR"
def digitos_aux(numf,num1,num2):
      while numf != 0:
            
            if numf%10 > 5:
                  num1 += 1
                  numf//=10
            if numf%10 <= 5:
                  num2 += 1
                  numf//=10
      return (num1,num2)
#2#############################################
def forma_par(num):
      if not isinstance(num,int):
            return "ERROR"
      result = 0
      potencia = 0

      while num != 0:
            if (num%10)%2 == 0:
                  
                  result += (num%10*10**potencia)
                  potencia+=1
                  num //=10
            else:
                  num//=10

      return result
                  
#3#############################################
def todos_pares(num):
      if not isinstance (num,int):
            return "ERROR"

      while num != 0:
            if (num%10)%2 == 1:
                  return False
            else:
                  num//=10
      
      return True
#4#############################################
def factorial(n):
      if not isinstance (n,int):
            return "ERROR"
      factor=1
      
      while n != 0:
            
            factor*=n
            n-=1
            
            
 
      return factor
#5#############################################
def fib(n):
      if  isinstance (n,int):
            return fib_aux(num,0)
      else:
             return "ERROR"
def fib_aux(num,fila):
      new = 1
      ultimo = 0

      while fila < n:

            b = new + ultimo
            new = ultimo
            ultimo = b
            fila = fila+1
      return b
      
      
            
            
 
      
#6#############################################
def palindromo(num):
      if isinstance(num,int):
            return palindromo_aux(num)
      else:
            return"ERROR"
def palindromo_aux(num):
      new = (len(num,0)-1)
      while num != 0:
            if (num%10) == (num//(10**new)):
                  num = num//10
                  num=num//(10**new)
                  new -= 1
            else:
                  return False
      return True

def len(num,fila):
      while num != 0:
            fila == 1
            num = num//10
      return fila

#7#############################################
def eliminar(dig,num):
      if isinstance(dig,int) and isinstance(num,int):
            return elimanr_aux(dig,num)
      else:
            return "ERROR"

def eliminar_aux(dig,num):
      T = True
      potencia = 0
      m = 0
      while T:
            if dig != num%10:
                  m += num%10*10**potencia
                  potencia += 1
                  num//=10
            else:
                  T = False
                  num//=10
      m += num*10*potencia
      return m











