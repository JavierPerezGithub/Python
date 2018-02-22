# -*- coding: utf-8 -*-
'''
Created on 2 feb. 2017

@author: profesoresi
'''
from Tkinter import *
from ttk import Combobox
import tkMessageBox

def saludar():
    saludo = opcion.get() + ' ' + sNombre.get() + ' ' + sApellidos.get() 
    print saludo
    tkMessageBox.showinfo("Saludo", saludo)

    texto1 = ''
    if checkvar1.get() == 1:
        texto1 = 'Elemento1 está seleccionado'
    else:
        texto1 = 'Elemento1 no está seleccionado'
    print texto1
    texto2 = ''
    if checkvar2.get() == 1:
        texto2 = 'Elemento2 está seleccionado'
    else:
        texto2 = 'Elemento2 no está seleccionado'
    print texto2
    print 'Desde ' + ciudad.get()
    print 'Tu edad es ' + str(edad.get())
    
def limpiar():
    sNombre.set('')
    sApellidos.set('')
    opcion.set('Hola')
    check1.deselect()
    check2.deselect()
    ciudad.set('')
    edad.set(1)
    
    
    
ventana = Tk()
ventana.title("Ventana Saludo")
ventana.geometry("400x300")

label_nombre = Label(ventana, text="Nombre")
label_nombre.place(x=10, y=10)
sNombre = StringVar()
caja_nombre = Entry(ventana, textvariable=sNombre, width="20")
caja_nombre.place(x=80, y=10)

label_apellidos = Label(ventana, text="Apellidos")
label_apellidos.place(x=10, y=30)
sApellidos = StringVar()
caja_apellidos = Entry(ventana, textvariable=sApellidos, width="40")
caja_apellidos.place(x=80, y=30)

opcion = StringVar() 
opcion.set('Hola') 
opcion1 = Radiobutton(ventana, text="Hola", value='Hola', variable=opcion)
opcion1.place(x=10, y=70) 
opcion2 = Radiobutton(ventana, text="Adios", value='Adios', variable=opcion)
opcion2.place(x=80, y=70)

checkvar1 = IntVar()  
checkvar2 = IntVar()
check1 = Checkbutton(ventana, text="Elemento1", variable=checkvar1, onvalue=1, offvalue=0)  
check2 = Checkbutton(ventana, text="Elemento2", variable=checkvar2, onvalue=1, offvalue=0)
check1.place(x=10, y=100) 
check2.place(x=120, y=100)

label_ciudad = Label(ventana, text="Ciudad")
label_ciudad.place(x=10, y=130)
ciudad = StringVar()  
combo = Combobox(ventana, values=('Madrid', 'Barcelona', 'Sevilla'), 
                 textvariable=ciudad, state="readonly")
combo.place(x=80,y=130)

label_edad = Label(ventana, text="Edad")
label_edad.place(x=10, y=160)
edad = IntVar()  
spin = Spinbox(ventana, from_=1, to=50, textvariable=edad, 
               state="readonly")
spin.place(x=80,y=160)

saludar = Button(ventana, text="Saludar", command=saludar)
saludar.place(x=100, y=190)
limpiar = Button(ventana, text="Limpiar", command=limpiar)
limpiar.place(x=170, y=190)

ventana.mainloop()



