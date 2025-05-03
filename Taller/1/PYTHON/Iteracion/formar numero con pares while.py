class Iteracion(object):
    def __init__ (self):
        pass
    def new_num(self,num):
        if isinstance(num,int):
            return self.new_num_aux(num)
        else:
            return "ERROR"

    def new_num_aux(self,num):
        potencia = 0
        resultado = 0
        while num > 0:
            if num %10 %2 == 0:
                
                resultado += (num % 10) * (10 ** potencia)
                potencia += 1
            
            num = num//10
            
                

        print(resultado)
      
