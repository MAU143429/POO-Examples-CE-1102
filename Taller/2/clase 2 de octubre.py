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
            return tienemas_par(lista,0,0,0)
      else:
            return "ERROR"
def tienemas_par_aux(lista,par,impar,indice):
      if len(lista) == indice:
            return

            
