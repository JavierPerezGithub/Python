'''
Created on 14/2/2018

@author: 5725
'''
from Tkinter import *

def saludo():
    print "Hola a todos"

def minimizar():
    ventana1.iconify()

ventana1 = Tk()
ventana1.title("Posicionamiento")
ventana1.geometry("400x200")
etiqueta1 = Label(ventana1, text="Desde aqui saludamos")
etiqueta1.place(x=10, y=10)
etiqueta2 = Button(ventana1, text="Dame clic para saludar", command = saludo).place(x=200, y=10)
etiqueta3 = Label(ventana1, text="Desde aqui minimizamos").place(x=10, y=50)
etiqueta4 = Button(ventana1, text="Dame clic para minimizar", command = minimizar).place(x=200, y=50)
ventana1.mainloop()