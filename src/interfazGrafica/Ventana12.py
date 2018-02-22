'''
Created on 14/2/2018

@author: 5725
'''
from Tkinter import *

def operacion():
    numero = num.get()
    if opcion.get() == 1:
        total = numero * 10
    elif opcion.get() == 2:
        total = numero * 20
    elif opcion.get() == 3:
        total = numero * 30
    elif opcion.get() == 4:
        total = numero * 40
    elif opcion.get() == 5:
        total = numero * 50
    else:
        total = numero * numero
    print "El total de la operacion es:" + str(total)
    
ventana = Tk()
#la variable opcion tomara diferentes valores dependiendo de la opcion seleccionada en el control Radiobutton
opcion = IntVar()
num = IntVar()
ventana.title("Radiobutton en tkinter")
ventana.geometry("400x300")
etiqueta1 = Label(ventana, text="Escribe el numero:").place(x=20, y=20)
cajaNumero = Entry(ventana, textvariable = num).place(x=180, y=20)
etiqueta2 = Label(ventana, text="Escribe la opcion:").place(x=20, y=50)
x10 = Radiobutton(ventana, text='X10', value = 1, variable = opcion).place(x=20, y=80)
x20 = Radiobutton(ventana, text='X20', value = 2, variable = opcion).place(x=70, y=80)
x30 = Radiobutton(ventana, text='X30', value = 3, variable = opcion).place(x=120, y=80)
x40 = Radiobutton(ventana, text='X40', value = 4, variable = opcion).place(x=20, y=110)
x50 = Radiobutton(ventana, text='X50', value = 5, variable = opcion).place(x=70, y=110)
cuadrado = Radiobutton(ventana, text='Cuadrado', value = 6, variable = opcion).place(x=120, y=110)
boton = Button(ventana, text = 'Realiza operacion', command = operacion).place(x=20, y =140)
ventana.mainloop()

