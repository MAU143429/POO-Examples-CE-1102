def sumaM(m,f,c,resultado):
    if f == len(m):
        return resultado
    elif c == len(m[0]):
        return sumaM(m,f+1,0,resultado)
    else:
        return sumaM(m,f,c+1,resultado+m[c][f])


def sum(m,f,r):
    if f == len(m):
        return r
    else:
        return sfila(m[f],o,r)+sum(m,f+1,r)
def sfila(fila,c,r):
    if c == len(fila):
        return r
    else: return sfila(fila,c+1,r+fila[c])



