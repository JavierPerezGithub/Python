'''
Created on 14/2/2018

@author: 5725
'''
from Tkinter import *

def saludar():
    print "Hola: " + nombre.get() 
ventana = Tk()
nombre = StringVar()
apellidoP = StringVar()
apellidoM = StringVar()

ventana.title("Entradas en tkinter")
ventana.geometry("400x400")
etiqueta1 = Label(ventana, text="Escribe tu nombre").place(x=10, y=10)
nombreCaja = Entry(ventana, textvariable=nombre).place(x=170, y=10)
boton = Button(ventana, text="Saludo personalizado", command = saludar).place(x=10, y=50)
ventana.mainloop()
