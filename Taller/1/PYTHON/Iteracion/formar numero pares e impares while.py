class Iteracion(object):
    def __init__ (self):
        pass
    def new_num(self,num):
        if isinstance(num,int):
            return self.new_num_aux(num)
        else:
            return "ERROR"

    def new_num_aux(self,num):
        potencia1 = 0
        potencia2 = 0
        pares = 0
        impares = 0
        while num > 0:
            if num %10 %2 == 0:
                pares += (num % 10) * (10 ** potencia1)
                potencia1 += 1
            elif num % 10 % 2 == 1:
                impares += (num % 10) * (10 ** potencia2)
                potencia2 += 1
                
                
            
            num = num//10
            
                

        print(pares)
        print(impares)
