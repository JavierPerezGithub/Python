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
        self.menuSel = ''   
        self.ventan21Creada = False     
        
        self.title("Ventana Python")
        self.geometry("600x400")
        self.createWidgets() 
 
    def createWidgets(self):         
        self.barramenu = Menu(self)
        
        self.primermenu = Menu(self.barramenu)
        self.primermenu.add_command(label="Submenú 11", command=self.accion1)
        self.primermenu.add_command(label="Submenú 12", command=self.accion2)
        self.primermenu.add_separator()
        self.primermenu.add_command(label="Salir", command=self.destroy)
        self.barramenu.add_cascade(label="Primer Menú", menu=self.primermenu)
        
        self.segundomenu = Menu(self.barramenu)
        self.segundomenu.add_command(label="Submenú 21", command=self.accion21)
        self.segundomenu.add_command(label="Submenú 22", command=self.accion22)
        self.barramenu.add_cascade(label="Segundo Menú", menu=self.segundomenu)
        
        self.config(menu=self.barramenu)
        

    def accion1(self):
        if self.menuSel == '21':
            self.limpiarMenu21()
        elif self.menuSel == '22':
            self.limpiarMenu22()
        self.menuSel = '11'
        self.ventanaAux = Tk()
        self.ventanaAux.geometry("300x150")
        self.ventanaAux.mainloop()
        
    def accion2(self):
        if self.menuSel == '21':
            self.limpiarMenu21()
        elif self.menuSel == '22':
            self.limpiarMenu22()
        self.menuSel = '12'
        print "Segundo men�"
        
    def accion21(self):
        if self.menuSel == '22':
            self.limpiarMenu22()
        
        if not self.ventan21Creada:
            self.crearVentana21()
        else:
            self.ventana21.place(x=0, y=0) 
            self.guardar["command"] = self.accGuardar
            self.limpiar["command"] = self.accLimpiar
            
        
    def crearVentana21(self): 
        self.ventana21 = Frame(self, width="600", height="400")
        self.ventana21.place(x=0, y=0)
        
        self.menuSel = '21'
        self.label_nombre = Label(self.ventana21, text="Nombre")
        self.label_nombre.place(x=30, y=20)
        self.sNombre = StringVar()
        self.caja_nombre = Entry(self.ventana21, textvariable=self.sNombre, 
                                 width="20")
        self.caja_nombre.place(x=120, y=20)

        self.label_apellidos = Label(self.ventana21, text="Apellidos")
        self.label_apellidos.place(x=30, y=50)
        self.sApellidos = StringVar()
        self.caja_apellidos = Entry(self.ventana21, textvariable=self.sApellidos, 
                                    width="40")
        self.caja_apellidos.place(x=120, y=50)
        
        self.label_categoria = Label(self.ventana21, text="Categoría")
        self.label_categoria.place(x=30, y=80)
        self.categoria = StringVar()  
        self.combo = Combobox(self.ventana21, values=('Amigos', 'Familia', 'Trabajo'), 
                 textvariable=self.categoria, state="readonly")
        self.combo.place(x=120,y=80)
        
        self.label_telefono = Label(self.ventana21, text="Teléfono")
        self.label_telefono.place(x=30, y=110)
        self.sTelefono = StringVar()
        self.caja_telefono = Entry(self.ventana21, textvariable=self.sTelefono, 
                                    width="20")
        self.caja_telefono.place(x=120, y=110)
        
        self.label_email = Label(self.ventana21, text="Email")
        self.label_email.place(x=30, y=140)
        self.sEmail = StringVar()
        self.caja_email = Entry(self.ventana21, textvariable=self.sEmail, 
                                    width="40")
        self.caja_email.place(x=120, y=140)
        
        self.guardar = Button(self.ventana21, text="Guardar", command=self.accGuardar)
        self.guardar.place(x=70, y=170)
        self.limpiar = Button(self.ventana21, text="Limpiar", command=self.accLimpiar)
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
            
            
    def accion22(self):
        if self.menuSel == '21':
            self.limpiarMenu21()
        self.menuSel = '22'
        self.label22 = Label(self, text="Etiqueta del menú 22")
        self.label22.place(x=30, y=20)
        
    def limpiarMenu21(self):
        '''self.label_nombre.destroy()
        self.caja_nombre.destroy()

        self.label_apellidos.destroy()
        self.caja_apellidos.destroy()
        
        self.label_categoria.destroy()
        self.combo.destroy()
        
        self.label_telefono.destroy()
        self.caja_telefono.destroy()
        
        self.label_email.destroy()
        self.caja_email.destroy()
        
        self.guardar.destroy()
        self.limpiar.destroy()'''
        self.ventana21.place_forget()
        
    def limpiarMenu22(self):
        self.label22.destroy()
        
app = Application() 
app.mainloop()

        