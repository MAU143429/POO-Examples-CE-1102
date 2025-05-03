
#1
def combinaciones(hp,dell):
    if isinstance(hp,list) and isinstance(dell,list)and len(hp)>0 and len(dell)>0:
        return combinaciones_aux(hp,dell)
    else: return "Los parametros no son listas o estan vacias"

def combinaciones_aux(hp,dell):
    if  hp == []:
        return []
    else: return comb_aux(hp[0], dell) + combinaciones_aux(hp[1:], dell)

def comb_aux(valor,dell):
    if dell == []:
        return []
    else: return [valor+dell[0]] + comb_aux(valor,dell[1:])


    
#1 cola
def combinaciones1(hp,dell):
    if isinstance(hp,list) and isinstance(dell,list)and len(hp)>0 and len(dell)>0:
        return combinaciones_aux(hp,dell,[])
    else: return "Los parametros no son listas o estan vacias"

def combinaciones_aux(hp,dell,result):
    if  hp == []:
        return result
    else: return (comb_aux(hp[0], dell,[])) +combinaciones_aux(hp[1:], dell,result)

def comb_aux(valor,dell,result2):
    if dell == []:
        return result2
    else: return comb_aux(valor,dell[1:],result2+[valor+dell[0]])

    


#2
import math
def std (lista,avg):
    if isinstance(lista,list) and isinstance(avg,float):
        return math.sqrt(std_aux(lista,avg)/len(lista)-1)
    else: return "ERROR"

def std_aux(lista,avg):
    if lista == []:
        return 0
    else:
        return(lista[0]-avg)**2+std_aux(lista[1:],avg)


    
#2 cola
import math
def std_cola (lista,avg):
    if isinstance(lista,list) and isinstance(avg,float):
        return math.sqrt(std_auxcola(lista,avg,0)/len(lista)-1)
    else: return "ERROR"

def std_auxcola(lista,avg,result):
    if lista == []:
        return result
    else:
        return std_aux((lista[1:],avg,result+lista[0]-avg)**2)

    


#3
def zScore(lista,S,avg):
    if isinstance(lista,list) and isinstance(S,float) and isinstance(avg,float):
        return zScore_aux(lista,S,avg)
    else:
        return "ERROR"

def zScore_aux(lista,S,avg):
    if lista == []:
        return []
    else:
        return [(lista[0]-avg)/S]+ zScore_aux(lista[1:],S,avg)


#3 cola

def zScore_cola(lista,S,avg):
    if isinstance(lista,list) and isinstance(S,float) and isinstance(avg,float):
        return zScore_auxcola(lista,S,avg,[])
    else:
        return "ERROR"

def zScore_auxcola(lista,S,avg,result):
    if lista == []:
        return result
    else:
        return zScore_aux(lista[1:],S,avg,result+[(lista[0]-avg)/S])


#4

def rScore(Zx,Zy):
    if isinstance(Zx,list) and isinstance(Zy,list) and len(Zx)== len(Zy):
        return (rScore_aux(Zx,Zy)/(len(Zx)-1))
    else:
        return "ERROR"
def rScore_aux(Zx,Zy):
    if Zx == [] and Zy == []:
        return 0
    else:
        return(Zx[0]*Zy[0])+rScore_aux(Zx[1:],Zy[1:])


#4 cola
    
def rScorecola(Zx,Zy):
    if isinstance(Zx,list) and isinstance(Zy,list) and len(Zx)== len(Zy):
        return (rScore_auxcola(Zx,Zy,0)/(len(Zx)-1))
    else:
        return "ERROR"
def rScore_auxcola(Zx,Zy,result):
    if Zx == [] and Zy == []:
        return result
    else:
        return rScore_aux(Zx[1:],Zy[1:],result+Zx[0]*Zy[0])
