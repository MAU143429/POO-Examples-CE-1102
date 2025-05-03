class Fig:
    def __init__(self):
        pass
    
    def __init__(self,x,y):
        self.x=x
        self.__y=y
    def getX(self):
        return self.x
    def setX(self,x):
        if x >= 0 and x <= 1023:
            self.__x = x
        else:
            print("Elvalor de x debe ser mayor o igual y menos a 1023.")

    def getY(self):
        return self.__y
    def setY(self,y):
        if y >= 0 and y <= 767:
            self.__y=y
        else: print("El valor de y debe ser mayor o igual a 0 y menor a 768.")
