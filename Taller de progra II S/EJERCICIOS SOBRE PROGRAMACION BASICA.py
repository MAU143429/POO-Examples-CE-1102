#1
#EL 1 LO VEO MEJOR DEBIDO SE UTLIZA IF ADINADOS Y ES MAS EFICIENTE QUE UTILIZART LOS IF INDEPENDIENTES Y QUE SE EJECUTEN UNO A UNO, EN SINTESIS EL RESULTADO ES EL MISMO.
#PERO EN MI OPINION UNA MAS OPTIMIZADA QUE LA OTRA

#2
def Area_Triangulo(base,altura):
  if isinstance(base,(int,float)) and isinstance(altura,(int,float)) and base > 0 and altura > 0:
    area = (base*altura)/2
    return area
  else:
    return "ERROR"

#3
def Notas_Intro(nota):
  if isinstance(nota,(int,float)):
    if nota > 70:
      return "Aprobado"
    else:
      return "Reprobado"
  else: "ERROR"

#4
def Notas_Tec(nota):
  if isinstance(nota,(int,float)):
    if nota >= 67.5:
      return "Aprobado"
    elif 67.5>nota>=60:
      return "Aplazado"
    else:
      return "Reprobado"
  else: "ERROR"
#5
def col_dol(colones):
  if isinstance(colones,(int,float)):
    return colones/582
  else: "ERROR"

def dol_col(dolares):
  if isinstance(dolares,(int,float)):
    return dolares*582
  else: "ERROR"

#6
def Temp_F(grados):
  if isinstance (grados,(int,float)):
    return ((grados-32)/9)*5
#7
def llave(num):
  if isinstance(num,(int,float)):
    return (num*1024**3)
  else: "ERROR"


#8
def sum_prom(num1,num2,num3,num4,num5):
  if isinstance(num1,(int,float)) and isinstance(num2,(int,float)) and isinstance(num3,(int,float)) and isinstance(num4,(int,float)) and isinstance(num5,(int,float)):
    suma=(num1+num2+num3+num4+num5)
    promedio= (num1+num2+num3+num4+num5)/5
    return (suma,promedio)
  else: "ERROR"
#9
def Rectangulo(base,altura):
  if isinstance (base,(int,float)) and isinstance (altura,(int,float)) and base >0 and altura>0:
    area= base*altura
    perimetro= (base+base)+(altura+altura)
    return (area,perimetro)
#10
def suma(num):
  if isinstance(num,(int,float)):
    num1=num%10
    num2=(num//10)%10
    num3=(num//100)%10
    return (num1+num2+num3)

  
   
      
    

  
