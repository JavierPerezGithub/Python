# -*- coding: utf-8 -*-

from Tkinter import Tk, Label, Button, StringVar
import time
from ttk import Combobox
import tkMessageBox

def accion():
    print tkMessageBox.showinfo("Mensaje","El valor seleccionado es: " + valor.get())


def accion2():
    ventana.destroy() 

ventana = Tk()
ventana.title("Ventana Python")
ventana.geometry("600x200")

valor = StringVar()  
combo = Combobox(ventana, values=("A", "B", "C"), textvariable=valor).place(x=10,y=10)


imprimir = Button(ventana, text="Imprimir", command=accion).place(x=10,y=40)
cierra = Button(ventana, text="Cerrar", command=accion2).place(x=80,y=40)

ventana.mainloop()
