'''
Created on 14/2/2018

@author: 5725
'''
from Tkinter import *

ventana1 = Tk()
ventana1.title("Posicionamiento")
boton = Button(ventana1, text="Posicionamiento diferente").grid(row=0, column=1)
etiqueta = Label(ventana1, text="Posicionamiento diferente").grid(row=0, column=0)
etiqueta2 = Label(ventana1, text="Posicionamiento diferente 2").grid(row=1, column=1)
etiqueta3 = Label(ventana1, text="Posicionamiento diferente 3").grid(row=4, column=4)
ventana1.mainloop()
