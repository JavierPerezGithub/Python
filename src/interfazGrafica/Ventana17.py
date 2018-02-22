# -*- coding: utf-8 -*-
'''
Created on 5 de feb. de 2017

@author: maria
'''
from Tkinter import * 
from ttk import Combobox


    

class Application(Tk):     
    
    def __init__(self):         
        Tk.__init__(self) 
        
        self.title("Ventana Python")
        self.geometry("600x400")
        self.createWidgets() 
        
        self.crearVentana1()
        self.crearVentana2()
        
 
    def createWidgets(self):         
        self.barramenu = Menu(self)
        
        self.primermenu = Menu(self.barramenu)
        self.primermenu.add_command(label="Submenú 11", command=self.accion1)
        self.primermenu.add_command(label="Submenú 12", command=self.accion2)
        self.primermenu.add_separator()
        self.primermenu.add_command(label="Salir", command=self.destroy)
        self.barramenu.add_cascade(label="Primer Menú", menu=self.primermenu)
        
        self.config(menu=self.barramenu)
        

    def crearVentana1(self):
        self.ventana1 = Frame(self, width="600", height="400")        
        self.label_nombre = Label(self.ventana1, text="Nombre")
        self.label_nombre.place(x=30, y=20)
        self.sNombre = StringVar()
        self.caja_nombre = Entry(self.ventana1, textvariable=self.sNombre, 
                                 width="20")
        self.caja_nombre.place(x=120, y=20)

        self.label_apellidos = Label(self.ventana1, text="Apellidos")
        self.label_apellidos.place(x=30, y=50)
        self.sApellidos = StringVar()
        self.caja_apellidos = Entry(self.ventana1, textvariable=self.sApellidos, 
                                    width="40")
        self.caja_apellidos.place(x=120, y=50)
        
        self.label_categoria = Label(self.ventana1, text="Categoría")
        self.label_categoria.place(x=30, y=80)
        self.categoria = StringVar()  
        self.combo = Combobox(self.ventana1, values=('Amigos', 'Familia', 'Trabajo'), 
                 textvariable=self.categoria, state="readonly")
        self.combo.place(x=120,y=80)
        
        self.label_telefono = Label(self.ventana1, text="Teléfono")
        self.label_telefono.place(x=30, y=110)
        self.sTelefono = StringVar()
        self.caja_telefono = Entry(self.ventana1, textvariable=self.sTelefono, 
                                    width="20")
        self.caja_telefono.place(x=120, y=110)
        
        self.label_email = Label(self.ventana1, text="Email")
        self.label_email.place(x=30, y=140)
        self.sEmail = StringVar()
        self.caja_email = Entry(self.ventana1, textvariable=self.sEmail, 
                                    width="40")
        self.caja_email.place(x=120, y=140)
        
        self.guardar = Button(self.ventana1, text="Guardar", command=self.accGuardar)
        self.guardar.place(x=70, y=170)
        self.limpiar = Button(self.ventana1, text="Limpiar", command=self.accLimpiar)
        self.limpiar.place(x=140, y=170)
        
    def accGuardar(self):
        print "guardar"
        # vamos a escribir todo de nuevo
        n = self.sNombre.get()
        ap = self.sApellidos.get()
        t = self.sTelefono.get()
        e = self.sEmail.get()
        cat = self.categoria.get()
        
        print "guardando " + n + "," + ap + "," + cat + "," + t + "," + e
    
    def accLimpiar(self):
        print "limpiar"
        self.sNombre.set("")
        self.sApellidos.set("")
        self.sTelefono.set("")
        self.sEmail.set("")
        self.categoria.set("")
    
    
    def crearVentana2(self):
        self.ventana2 = Frame(self, width="600", height="400")
        self.label_1 = Label(self.ventana2, text="Etiqueta 1")
        self.label_1.place(x=30, y=20)
        self.label_2 = Label(self.ventana2, text="Etiqueta 2")
        self.label_2.place(x=30, y=50)
        
    def accion1(self):
        self.ventana2.place_forget()
        
        self.ventana1.place(x=0, y=0) 
        self.guardar["command"] = self.accGuardar
        self.limpiar["command"] = self.accLimpiar
        
    def accion2(self):
        self.ventana1.place_forget()
        
        self.ventana2.place(x=0, y=0)
        
        
app = Application() 
app.mainloop()

        