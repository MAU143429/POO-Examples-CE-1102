#Importamos librerias necesarias
import tkinter
import os
import time
from tkinter import *
from tkinter import messagebox             #En dicho espacio lo que se hace es importar las difernetes librerias y modulos.+
from tkinter.simpledialog import askstring
from pandas import *
import pandas as pd
import csv
##############################################################


#creacion de ventana y canva
window= Tk()   #define y crea la ventana
window.title("Vending Machine") #damos titulo a la ventana
imgbg=PhotoImage(file="Images/fondo.png")     #ae cargan imagenes
imgbg3=PhotoImage(file="Images/botonera.png") #y se convierte en variable
canvas = Canvas(window,width=800, height=500)
canvas.pack(expand=YES, fill=BOTH)
Label(window,image=imgbg).place(x=0,y=0)   #se crea una etiqueta para los backgrounds
Label(window,image=imgbg3).place(x=490,y=10) #una para la botonera y otra el bg total
###############################################################
fuente=("ARIAL 27")
fuente1 =("ARIAL 22")
fuente2 =("ARIAL 14") # se crean unas variables para tipos de funtes
fuente3=("ARIAL 10")
#Funcones
#ADMIN#########################################################
# Todo el codigo que sigue pertence a la pantalla de administrador
def login():  # se define login
    window.withdraw()   #se utliza para eliminar la ventana anterior
    window2 = Toplevel()  #Este metodo me permite suoerponer la ventana nueva
    window2.title("Login")  #titulo de la ventana
    window2.geometry("20x30") #dimensiones de la ventana
    window2.configure(bg="blue") # se configura el fondo
    entrada= askstring("Password","Insert Password",show="*") # se crea la variable entrada que servira para verficar la contraseña
       
    def validar(entrada1): # se define una funcion para validar los parametros de entradas
        if entrada1 == "1434": # se define la condicion de la contraseña
            window2.withdraw() # se destruyela ventana
            Administrador()
        else:
            messagebox.showwarning("Warning!!","ERROR WRONG PASSWORD ")# lanza mensaje de error en contraseña

    btnvali = Button(window2,width=10,height=1,text=" CONFIRM ", command= lambda entrada1=entrada: validar(entrada1)).pack()#boton de validacion de la contraseña a segundo paso
                

def Administrador(): #se define la funcion de administrador
    def Apagar(): # se define una funcion para apagar maquina
        window3.withdraw() # se destruye el modo administratid
    window3 = Toplevel() # se superponen las ventanas
    window3.title("Admnistrador") #se define titulo de la ventana   
    window3.geometry("800x500") #se define dimensiones de la nueva ventana
    window3.configure(bg="blue")#se configura el background
    imgbg2=PhotoImage(file="Images/fondo.png")# se carga la imagen 
    Label(window3,image=imgbg2).place(x=0,y=0)# se crea un label y se pone como fondo
    btnAP= Button(window3,text= "POWER OFF",width=10,height=2,font = fuente3, command= Apagar).place(x=350,y=360) # boton de apagar el modo administrador
    btnRE= Button(window3,text= "RESET",width=10,height=2,font = fuente3, command= Reset ).place(x=350,y=280)# boton de reset el modo administrador
    btnVD= Button(window3,text= "SELLING REPORTS DETAIL",width=30,height=2,font = fuente3,command=V_Detallada).place(x=270,y=200)# boton de reporte de ventas resumen a}modo administrador
    btnVR= Button(window3,text= "SALES REPORT",width=30,height=2,font = fuente3, command= V_Resumen).place(x=270,y=100)# boton de areporte de ventas detallado a}modo administrador
    window3.mainloop()


        
#CARGA DE DATOS####################################################################   
def Reset(): # e define la funcion reset del sistema
    restart=[["Código","Descripción","Exstencias","Maxima","Costo" ,"Precio","Venta"],
            [1,"Audifonos Iphone",15,15,4500,6000,0],
            [2,"Cargador Samsung",15,15,1900,2500,0],
            [3,"Airpods Iphone" ,15,15,6500,10000,0],
            [4,"Llave maya 32 GB",15,15,2000,2500,0],
            [5,"Llave maya 64 GB",15,15,4000,5000,0],
            [6,"AppleWatch",15,15,6850,9000,0],
            [7,"Micro SD",15,15,750,2000,0],
            [8,"Ipad",15,15,7000,12500,0],
            [9,"Powerbank",15,15,3000,5000,0],
            [10,"Adaptador USB tipo a Jack",15,15,1500,3000,0],  # se carga una replica de la matriz original con los datos
            [11,"Funda Iphone",15,15,2000,3000,0],
            [12,"Disco Duro" ,15,15,5500,7500,0],
            [13,"Parlante Bluetooth",15,15,2990,4500,0],
            [14,"Go Pro" ,15,15,10.000,15000,0],
            [15,"Chrome Cast",15,15,4300,8500,0],
            [16,"Cable HDMI",15,15,2.600,4500,0]]
    myFile = open("Productos.csv","w")
    with myFile:
        writer = csv.writer(myFile) # se utiliza para sobreescribor los archivos de pyton a csv
        writer.writerows(restart)
def V_Detallada():
    main1 = Toplevel()
    main1.title("Venta Detallada")# se crea una nueva ventana, sus dimensiones y titulo
    main1.geometry("470x450") 
    Datos1= pd.read_csv("Venta Detallada.csv",header = 0)
    Data = Label(main1,text=Datos1,justify=LEFT,bg="#76FF03",width = 70,height = 30).place(x=0,y=0) #se crea label que muestra los datos en pantalla
def V_Resumen():
    main2 = Toplevel() # se crea una nueva ventana, dimensiones , y titulo
    main2.title("Venta Resumen")
    main2.geometry("470x400")
    Datos2= pd.read_csv("Venta Resumen.csv",header = 0)# se cargan los archivo y se ejecutan en un label
    Data = Label(main2,text=Datos2,justify=LEFT,bg="#76FF03",width = 70,height = 30).place(x=0,y=0)
    
    print(Datos2)
    
    
def Tabla2():
    Trans=(pd.read_csv("",header = 2))#carga tabla de movimientos
    print(Trans)
def Tabla3():
    billete=(pd.read_csv("Billete.csv",header = 3))#carga tabla de billetes
    print(billete)


def salir():# se sale del programa
    window.withdraw()

######################################################################################################
lista=pd.read_csv("Productos.csv",header = 0)#carga el archivo
et1_var = IntVar() #crea una varible de int var
et1 = Entry(window,textvariable=et1_var,width=2,font=fuente).place(x=610,y=375)# entry principal del codigo del preducto
PantallaCobro = Entry(window,width=10,font=fuente,justify= CENTER).place(x=527,y=42)# entry de pantalla de cobro
def total(): # se deine la funcion total
    
    producto=(" ")
    producto = et1_var.get()# se extrae el numero del producto que se desea comprar

    lista=pd.read_csv("Productos.csv",header = 0)#se carga la lista de productos
    print(producto)

    
    precio = lista["Precio"][producto] # se crea la variable del precio del producto
    print(precio)
    

    def dosmil():# resta 2000 al precio total
        precio -= 2000
    def mil():# resta 1000 al precio total
        precio -= 1000
    def quinientos():# resta 500 al precio total
        precio -=  500

billete1= PhotoImage(file="Images/b1.png")
billete2= PhotoImage(file="Images/b2.png")
billete3= PhotoImage(file="Images/m1.png")#carga imagenes y botones de billetes
b1btn= Button(window,image=billete1).place(x=498,y=130)
b2btn= Button(window,image=billete2).place(x=665,y=130)
m1btn= Button(window,image=billete3).place(x=609,y=130)

entclick = Button(window,text="BUY",bg="green",command=total).place(x=560,y=440) #boton de comprar
entclick = Button(window,text="EXIT",bg="red",command = salir).place(x=670,y=440)  # boton de salir






##Tarjeta############################################################################################
def tarjeta(): # define la funcion de compra por tarjeta

    pago= Tk()   #define y crea la ventana
    pago.title("Transaccion") #damos titulo a la ventana
    pago.configure(bg="#B388FF") #bg de la ventana
    pago.geometry("260x50")
    Label(pago,text= "PROCESSING....",bg="#B388FF",width = 19,height=2,font= fuente2).place(x=30,y=0)#label de procesando
    def compuerta():
        Label(pago,text= "YOUR PURCHASE WAS SUCCESSFUL",bg="#B388FF",width= 35,height=2,font="ARIAL 9").place(x=0,y=0)
        time.sleep(3)
        Label(window,text= "TAKE YOUR PRODUCT",bg="#B388FF",width= 19,height=2,font= fuente2).place(x=525,y=40)  # se define el proceso de pago con tarjeta
    d1 = Button(window,text= "PRESS TO OPEN THE GATE",bg="gray",command=compuerta).place(x=545,y=270)
    pago.withdraw
################################################################   
#Cargar imagenes
imgbtn1 = PhotoImage(file="Images/1.png")
imgbtn2 = PhotoImage(file="Images/2.png")
imgbtn3 = PhotoImage(file="Images/3.png")
imgbtn4 = PhotoImage(file="Images/4.png")
imgbtn5 = PhotoImage(file="Images/5.png")
imgbtn6 = PhotoImage(file="Images/6.png")
imgbtn7 = PhotoImage(file="Images/7.png")
imgbtn8 = PhotoImage(file="Images/8.png")
imgbtn9 = PhotoImage(file="Images/9.png")
imgbtn10= PhotoImage(file="Images/10.png")   #se cargan las imagenes
imgbtn11= PhotoImage(file="Images/11.png")
imgbtn12= PhotoImage(file="Images/12.png")
imgbtn13= PhotoImage(file="Images/13.png")
imgbtn14= PhotoImage(file="Images/14.png")
imgbtn15= PhotoImage(file="Images/15.png")
imgbtn16= PhotoImage(file="Images/16.png")
usrbtn= PhotoImage(file="Images/user.png")
trj1= PhotoImage(file="Images/visa.png")
trj2= PhotoImage(file="Images/mastercard.png")
trj3= PhotoImage(file="Images/americanexpress.png")

######################################################################

#Creacion de botones
c1 = Button(window,image=imgbtn1).place(x=10,y=10)
c2 = Button(window,image=imgbtn2).place(x=10,y=130)
c3 = Button(window,image=imgbtn3).place(x=10,y=250)
c4 = Button(window,image=imgbtn4).place(x=10,y=370)
c5 = Button(window,image=imgbtn5).place(x=130,y=10)
c6 = Button(window,image=imgbtn6).place(x=130,y=130)
c7 = Button(window,image=imgbtn7).place(x=130,y=250)
c8 = Button(window,image=imgbtn8).place(x=130,y=370)
c9 = Button(window,image=imgbtn9).place(x=250,y=10)
c10 = Button(window,image=imgbtn10).place(x=250,y=130)  # se crean lso botones
c11 = Button(window,image=imgbtn11).place(x=250,y=250)
c12 = Button(window,image=imgbtn12).place(x=250,y=370)
c13 = Button(window,image=imgbtn13).place(x=370,y=10)
c14 = Button(window,image=imgbtn14).place(x=370,y=130)
c15 = Button(window,image=imgbtn15).place(x=370,y=250)
c16 = Button(window,image=imgbtn16).place(x=370,y=370)
userbtn= Button(window,image=usrbtn, command = login).place(x=760,y=460)
trjbtn1= Button(window,image=trj1,command = tarjeta).place(x=518,y=210)
trjbtn2= Button(window,image=trj2,command = tarjeta).place(x=605,y=210)
trjbtn3= Button(window,image=trj3,command =tarjeta).place(x=695,y=210)
#Precios###############################################################
prod1 = Label(window,text="1.₡6000",bg="#1976D2",font=fuente3).place(x=30,y=105)
prod2 = Label(window,text="2.₡2500",bg="#1976D2",font=fuente3).place(x=30,y=225)
prod3 = Label(window,text="3.₡10000",bg="#1976D2",font=fuente3).place(x=30,y=345)
prod4 = Label(window,text="4.₡2500",bg="#1976D2",font=fuente3).place(x=30,y=465)
prod5 = Label(window,text="5.₡5000",bg="#1976D2",font=fuente3).place(x=150,y=105)
prod6 = Label(window,text="6.₡9000",bg="#1976D2",font=fuente3).place(x=150,y=225)
prod7 = Label(window,text="7.₡2000",bg="#1976D2",font=fuente3).place(x=150,y=345)
prod8 = Label(window,text="8.₡12500",bg="#1976D2",font=fuente3).place(x=150,y=465)
prod9 = Label(window,text="9.₡5000",bg="#1976D2",font=fuente3).place(x=270,y=105)  # se crea un label con el precio del producto
prod10 = Label(window,text="10.₡3000",bg="#1976D2",font=fuente3).place(x=270,y=225)
prod11 = Label(window,text="11.₡3000",bg="#1976D2",font=fuente3).place(x=270,y=345)
prod12 = Label(window,text="12.₡7500",bg="#1976D2",font=fuente3).place(x=270,y=465)
prod13 = Label(window,text="13.₡4500",bg="#1976D2",font=fuente3).place(x=390,y=105)
prod14 = Label(window,text="14.₡15000",bg="#1976D2",font=fuente3).place(x=380,y=225)
prod15 = Label(window,text="15.₡8500",bg="#1976D2",font=fuente3).place(x=390,y=345)
prod16 = Label(window,text="16.₡4500",bg="#1976D2",font=fuente3).place(x=390,y=465)
Prod = Label(window,text="INSERT CODE:",bg="gray").place(x=590,y=350)
Mpag = Label(window,text="PAY METHOD:",bg="gray").place(x=575,y=94)
Efec = Label(window,text="CASH:",bg="gray").place(x=498,y=104)
Tarjeta = Label(window,text="CREDIT CARD:",bg="gray").place(x=498,y=184)






window.mainloop()
