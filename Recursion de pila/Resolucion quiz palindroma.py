class Pali(object):
    def __init__ (self):
        pass


    def palindromo(self, lista):
        if isinstance(lista, list) and (len(lista)>0):
            return self.palindromo_aux(lista)
        else: return "EL PARAMETRO NO ES UNA LISTA"

    def palindromo_aux(self, lista):
        if (lista == [] or len(lista)==1):
            return "TRUE"
        elif(lista[0] == lista [-1]):
            return self.palindromo_aux(lista[1:-1])
        else: return "FALSE"



    def promedio(self, numero , largo):
        if isinstance(numero, int):
            return self.suma_aux(numero)/ largo
        else: return "EL VALOR NO ES UN ENTERO"

    def suma_aux(self, numero):
        if numero == 0:
          return 0
        else:return numero % 10 + self.suma(numero // 10)
