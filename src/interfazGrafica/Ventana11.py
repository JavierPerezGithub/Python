'''
Created on 14/2/2018

@author: 5725
'''
from Tkinter import *

def saludar():
    print "Hola: " + nombre.get() +" tienes " + str(edad.get())
ventana = Tk()
nombre = StringVar()
edad = IntVar()

ventana.title("Entradas en tkinter")
ventana.geometry("400x400")
etiqueta1 = Label(ventana, text="Escribe tu nombre").place(x=10, y=10)
nombreCaja = Entry(ventana, textvariable=nombre).place(x=170, y=10)
etiqueta2 = Label(ventana, text="Escribe tu edad").place(x=10, y=50)
EdadCaja = Entry(ventana, textvariable=edad).place(x=170, y=50)
boton = Button(ventana, text="Saludo personalizado", command = saludar).place(x=10, y=90)
ventana.mainloop()
