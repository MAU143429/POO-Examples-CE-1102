class Iteracion(object):
    def __init__ (self):
        pass
    def almacenar(self,num):
        if isinstance(num,int):
            return self.pares_While(num)
        else:
            return "ERROR"

    def pares_While(self,num):
        pares = []
        impares = []
        while num > 0:
            if num %10 %2 == 0:
                pares= pares + [num%10]
            elif num % 10 % 2 == 1:
                  impares= impares + [num%10]
            num= num//10
                

        print(pares)
        print(impares)
            
                
