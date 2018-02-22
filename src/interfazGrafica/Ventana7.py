'''
Created on 14/2/2018

@author: 5725
'''
from Tkinter import *

ventana1 = Tk()
ventana1.title("Posicionamiento")
etiqueta1 = Label(ventana1, text="Posicionamiento diferente 1").place(x=10, y=10)
etiqueta2 = Label(ventana1, text="Posicionamiento diferente 2").place(x=200, y=10)
etiqueta3 = Label(ventana1, text="Posicionamiento diferente 3").place(x=10, y=50)
etiqueta4 = Label(ventana1, text="Posicionamiento diferente 4").place(x=200, y=50)
ventana1.mainloop()
