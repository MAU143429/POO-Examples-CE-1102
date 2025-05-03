def serie(num):
    if isinstance(num,int):
        return serie_aux(num,0,[],2)
    else:
        return "ERROR"
def serie_aux(num,contador,result,base):
    if contador == num:
        return result
    if (base%10)%2 == 0:
        return serie_aux(num,contador+1,result+base+2)
