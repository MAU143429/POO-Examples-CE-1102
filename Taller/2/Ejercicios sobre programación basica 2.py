import math
#1
def esfera(radio):
  if isinstance (radio,(int,float)):
    volumen = (4/3*math.pi*radio**3)
    area= 4*math.pi*radio**2
    return (volumen,area)
#2
def aumenta(num,por):
  if isinstance (num,(int,float)) and isinstance (por,(int,float)):
    return (num/100)*(por+100)

#3
  
def adjunto(num,dig):
  if isinstance (num,int) and isinstance (dig,int):
    return ((num//num**10)**10)+(dig**1)

#4
def romano (num):
  if isinstance (num,int):
    if num == 1:
      return "I"
    if num == 2:
      return "II"
    if num == 3:
      return "III"
    if num == 4:
      return "IV"
    if num == 5:
      return "V"
    if num == 6:
      return "VI"
    if num == 7:
      return "VII"
    if num > 7:
      return "ERROR"

#5
def convertir(metros,indicador):
  if isinstance(metros,(int,float)) and indicador <= 4 and indicador >0:
    if indicador == 1:
      return metros*100 
    if indicador == 2:
      return (metros*100)/2.34
    if indicador == 3:
      return ((metros*100)/2.34)/12
    if indicador == 4:
      return (((metros*100)/2.34)/12)/3

  else:
    return "ERROR"
#6
def calc_salario(horas,tarifa):
  if isinstance (horas,(int,float)) and isinstance(tarifa,(int,float)):
    if horas <= 40:
      return horas*tarifa
    else:
      return horas*(tarifa/100)*150
#7
def tabla(num):
  if isinstance(num,int):
    print(str(num)+("x1=")+str(num*1))
    print(str(num)+("x2=")+str(num*2))
    print(str(num)+("x3=")+str(num*3))
    print(str(num)+("x4=")+str(num*4))
    print(str(num)+("x5=")+str(num*5))
#8
def num_letras (num):
  if isinstance (num,int):
    if num == 1:
      return "UNO"
    if num == 2:
      return "DOS"
    if num == 3:
      return "TRES"
    if num == 4:
      return "CUATRO"
    if num == 5:
      return "CINCO"
    if num > 6:
      return "ERROR"
#9
def bisiesto(año):
  if isinstance(año,int):
    if año%4 == 0 and año%100!=0 or año%400== 0:
      return "SI ES BISIESTO"
    else:
      return "NO ES BISIESTO"
#10
def orden(num1,num2,num3):
  if isinstance(num1,(int,float)) and isinstance(num2,(int,float)) and isinstance(num3,(int,float)):
    x= num1
    y= num2
    z= num3


#11
def invertir(num):
  if isinstance (num,(int,float)):
    potencia=1
    num1=num%10
    num2=((num//10)%10)
    num3=((num//100)%10)
    return (num1**potencia)+(num2**(potencia+10))+(num3**(potencia+1))
    
    
    
