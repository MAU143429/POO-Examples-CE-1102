class Operacion:
    def __init__(self):
        pass

    def par3(self,num):
        if isinstance(num, int):
            return self.par3_aux(num, 0 ,0)
        else:return "ERROR EL NUMERO NO ES UN ENTERO"


    def par3_aux(self,num,potencia,result):

        if num == 0:
            return result

        elif (num % 10) % 3 == 0:
            return self.par3_aux(num // 10, potencia,result)
        else:
            return self.par3_aux((num // 10), potencia + 1, (result + num % 10 * 10 ** potencia))
    
