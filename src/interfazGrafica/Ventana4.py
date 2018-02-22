'''
Created on 14/2/2018

@author: 5725
'''
from Tkinter import *
import time


def parpadear():
    ventana1.iconify()
    time.sleep(3)
    ventana1.deiconify()


ventana1 = Tk()
ventana1.title("Primera ventana con Tkinter")
boton = Button(ventana1, text="Evento", command=parpadear)
boton.pack()
ventana1.mainloop()
