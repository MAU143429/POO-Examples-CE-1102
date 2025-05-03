import tkinter
from tkinter import *

#Window####################################
ventana= Tk()
ventana.title("Idioma")
ventana.geometry("200x200")
imgbg=PhotoImage(file="Images/fondo2.png")
Label(ventana,image=imgbg).place(x=0,y=0)
et1 = Label(ventana,text="SELECCIONE EL IDIOMA",bg="#B9F6CA").place(x=40,y=20)
et2 = Label(ventana,text="SELECT LENGUAGE",bg="#B9F6CA").place(x=50,y=40)
def Español():
    ventana.destroy()
    import ES as ES
    

def Ingles():
    ventana.destroy()
    import EN as EN


#Imagenes y botones########################

Espa = PhotoImage(file="Images/espa.png")
Ing = PhotoImage(file="Images/Ing.png")
Espabtn = Button(ventana,image=Espa,command = Español).place(x=50,y=70)
Inbtn = Button(ventana,image=Ing,command = Ingles).place(x=50,y=120)




ventana.mainloop()
