class Figura(object):
    def __init__(self):
        pass
    def crear(self,n,m):
        if isinstance (n,int) and isinstance(m,int):
            return self.asterisco_aux(n,m)
        else:
            return "ERROR"
    def asterisco_aux(self,n,m):
        for fila in range(n):
            for col in range(m):
                if fila == 0 or fila == (n-1):
                    print("*", end==" ")
                elif col == 0 or col == (m-1):
                    print ("*", end ==" ")
                else: print ("*", end ==" ")

            print("")
                    
                    
               
        print(matriznew)
