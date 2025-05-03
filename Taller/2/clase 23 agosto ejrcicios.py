'''
Instituto Tecnológico de Costa Rica
Introduccion a la Programación
Jose Antonio Espinoza Chaves
2019083698

'''
#1)
#E:un numero entero
#S: un numero formado solo por unos
#R:-
def forme1 (num):
  if isinstance (num,int):
    return forme_aux(num,0)
  else:
    return 'Error'
def forme_aux(num,e):
  if num == 0:
    return 0
  if num%10 == 1:
    return num%10 * 10 ** e + forme_aux(num//10,e+1)
  else:
    return forme_aux(num//10,e)
#2)
#E:dos numeros
#S:bool, true si es mayor igual a num2, false si no
#R:-
def sumax(n1,n2):
  if isinstance(n1,int) and isinstance(n2,int):
    return sumax_aux(n1) >= n2
  else:
    return 'Error'
def sumax_aux(n1):
  if n1 == 0:
    return 0
  else:
    return n1%10 + sumax_aux(n1//10)
#3)
#E:dos numeros
#S:multiplica el numero 1 por el numero 2 pero por suma sucesiva
#R:--
def multi (num1,num2):
  if isinstance(num1,(int,float)) and isinstance(num2,(int)):
    return multi_aux(num1,num2,0)
  else:
    return 'Error'
def multi_aux(num1,num2,e):
  if num2== e:
    return 0
  else:
    return num1 + multi_aux(num1,num2,e+1)
def largo (num):
  if isinstance (num,int):
    return largo_aux(num)
  else:
    return 'Error'
def largo_aux(num):
  if num == 0:
    return 0
  else:
    return 1 + largo_aux(num//10)
#4)
#E:un numero entero
#S:tupla(suam de pares,suma de impares)
#R:debe ser entero
def sume_parimpar(num):
  if isinstance (num,int):
    return sumapar(num),sumaimpar(num)
  else:
    return 'Error'
def sumapar(num):
  if num == 0:
    return 0
  if num%10 % 2 == 0:
    return num%10 + sumapar(num//10)
  else:
    return sumapar(num//10)
def sumaimpar(num):
  if num == 0:
    return 0
  if num%10 %2 != 0:
    return num%10 + sumaimpar(num//10)
  else:
    return sumaimpar(num//10)
#5)
#E:numero entero
#S:el numero con un menos 1 en cada dígito
#R:debe ser entero
def reste1 (num):
  if isinstance (num,int):
    return reste1_aux(num,0)
  else:
    return 'Error'
def reste1_aux(num,e):
  if num == 0:
    return 0
  elif num%10 == 0:
    return num%10*10**e + reste1_aux(num//10,e+1)
  else:
    return (num%10-1)*10**e + reste1_aux(num//10,e+1)
#6)
#E:un numero entero y una cantidad de elevados
#S:el resultado de la sumatoria
#R:--
def formula (num,n):
  if isinstance (num,int) and isinstance (n,int):
    return 1+formula_aux(num,n,0)
  else:
    return 'Error'
def formula_aux(num,n,i):
  if i == n-1:
    return 0
  else:
    return num**i + formula_aux(num,n,i+1)










  
