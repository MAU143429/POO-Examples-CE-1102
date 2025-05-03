class Suma (object):
    def __init__(self):
        pass

    def sumaFor(self,L1,L2):
        if isinstance(L1,list) and isinstance(L2,list) and len(L1)==len(L2) :
            resultado = []
            
            for indice in range(len(L1)):
                resultado += [L1[indice]+L2[indice]]
                
        
            print(resultado)        
       

