from tkinter import *
import time



#Creación de la ventana y su dimensión
ventana = Tk()
ventana.title("Juego de Memoria")
ventana.geometry("900x500")


imagen = PhotoImage(file="fondo.png")

imgbtn1 = PhotoImage(file="Detras.png")
imgbtn2 = PhotoImage(file="Detras.png")
imgbtn3 = PhotoImage(file="Detras.png")
imgbtn4 = PhotoImage(file="Detras.png")
imgbtn5 = PhotoImage(file="Detras.png")
imgbtn6 = PhotoImage(file="Detras.png")

fondo = Label(ventana,image=imagen).place(x=0,y=0)

def info ():
    imginfo = PhotoImage(file = "ficha.png")
    print(imginfo)
    


c1 = Button(ventana,image=imgbtn1).place(x=150,y=40)
c2 = Button(ventana,image=imgbtn2).place(x=423,y=40)
c3 = Button(ventana,image=imgbtn3).place(x=680,y=40)
c4 = Button(ventana,image=imgbtn4).place(x=150,y=270)
c5 = Button(ventana,image=imgbtn5).place(x=423,y=270)
c6 = Button(ventana,image=imgbtn6).place(x=680,y=270)

imguser = PhotoImage(file= "user.png")
b=Button(ventana,image=imguser,command = info).place(x=850,y=450)




    





















ventana.mainloop()

