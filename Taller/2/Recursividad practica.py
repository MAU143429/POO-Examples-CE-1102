#1 PARTE!

#1
#Es cuando una funcion se llama asi misma varias veces

#Condicion que determina cuando termina el algoritmo.

#2

#Error al programar la condicion de parada,esta mal limitada Y retorna valores infinitos.

#3

#Hace a la funcion mas optimizada y nos permite separar procesos como verificar y luego procesar.


#2 PARTE

#1
def largo(num):
  if isinstance (num,(int,float)):
    return largo_aux(num,)
  else:
    return "ERROR"
def largo_aux(num):
  if num == 0:
    return 0
  else:
    return 1+largo_aux(num//10)

#2
def cuente_dig(num, dig):
  if isinstance (num,(int,float)) and isinstance(dig,(int,float)):
    return cuente_dig_aux(num,dig)
  else:
    return "ERROR"
def cuente_dig_aux(num,dig):
  if num == 0:
    return 0
  elif num%10 == dig:
    return 1+cuente_dig_aux(num//10,dig)
  else:
    return cuente_dig_aux(num//10,dig)
#3
def cuente_par(num):
  if isinstance (num,(int,float)):
    return cuente_par_aux(num)
  else:
    return "ERROR"
def cuente_par_aux(num):
  if num == 0:
    return 0
  elif num%10%2 == 0:
    return 1+cuente_par_aux(num//10)
  else:
    return cuente_par_aux(num//10)
#4
def iguales(num):
  if isinstance(num,(int,float)):
    return iguales_aux(num)
  else:
    return "ERROR"
def iguales_aux(num):
  u=num%10
  if u == num:
    return True
  else:
    return False
  
  if num < 10:
    return 0
  else:
    iguales_aux(num)
  
  
#5
def suma_impar(num):
  if isinstance(num,(int,float)):
    return suma_impar_aux(num)
  else:
    return "ERROR"
def suma_impar_aux(num):
  if num == 0:
    return 0
  if num%10%2 == 1:
    return num%10 +suma_impar_aux(num//10)
  else:
    return suma_impar_aux(num//10)



#5












