#1####################################################
def vector_invert(v):
      if isinstance (v,list):
            return vector_invert_aux(v,len(v)-1,len(v),[])
      else:
            return "ERROR"

def vector_invert_aux(v,c,m,new):
      if c == -1:
            return new
      else:
            v.append(c) + vector_invert_aux(v,c,m,new)


#2###################################################
def prod_escalar(num,lista):
      if isinstance(num,int) and isinstance (lista,list):
            return prod_escalar_aux(num,lista,[],0)
      else:
            return "ERROR"

def prod_escalar_aux(num,lista,result,indice):
      if len(lista) == indice:
            return result
      else:
            return prod_escalar_aux(num,lista,result + [num*lista[indice]],indice+1)

#3##################################################
def prod_vector(lista,lista1):
      if isinstance(lista,list) and isinstance (lista1,list) and (len(lista)==len(lista1)):
            return prod_vector_aux(lista,lista1,0,0)
      else:
            return "ERROR"

def prod_vector_aux(lista,lista1,result,indice):
      if len(lista) == indice:
            return result
      else:
            return prod_vector_aux(lista,lista1,result + (lista[indice]*lista1[indice]),indice+1)
      
#4##################################################
def tienemas_par(lista):
      if isinstance(lista,list):
            return tienemas_par_aux(lista,0,0,0)
      else:
            return "ERROR"
def tienemas_par_aux(lista,par,impar,indice):
      if indice == len(lista) and par>impar:
            return True
      else:
            return False

      if (lista[indice])%10%2 == 0:
            return tienemas_par_aux(lista,par+1,impar,indice+1)
      else:
            return tienemas_par_aux(lista,par,impar+1,indice+1)
      
#5##################################################

def inn(lista,lista1):
      if isinstance(lista,list) and isinstance (lista1,list):
            return inn_aux(lista,lista1,0)
      else:
            return "ERROR"
#def inn_aux(lista,lista1,indice)

#6##################################################
def ordenado(lista):
      if isinstance(lista,list):
            return ordenado_aux(lista,0)
      else:
            return "ERROR"
def ordenado_aux(lista,indice):
      if indice == len(lista):
            return True

      if (lista[indice])%10 < lista[indice]%100:
            return orden_aux(lista,indice+1)
      else:
            return False

#7##################################################
#8##################################################
def matriz_promedio(lista):
      if isinstance(lista,list):
            return recorrer_aux(lista,0,0,0)
      else:
            return "ERROR"


def recorrer_aux(lista,result,indice,contador):
      if indice == len(lista):
            return (result/contador)
      elif isinstance(lista[indice],list):
            return (recorrer_aux(lista[indice],0,0,0) + recorrer_aux(lista,result,indice+1,contador+1))
      else:
            return recorrer_aux(lista,result+lista[indice],indice+1,contador+1)
#9##################################################
def dia_matriz(matriz):
        if isinstance(matriz,list):
            return dia_matriz_aux(matriz,0,[])
        else:
            return "ERROR"
def dia_matriz_aux(matriz,indice,result):
      if indice == len(matriz):
            return result
      else:
            return dia_matriz_aux(matriz,indice+1,result+[matriz[indice][indice]])

      
