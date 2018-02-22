# -*- coding: utf-8 -*-
'''
Created on 9 feb. 2017

@author: profesoresi
'''
from Tkinter import Tk, Menu, Label
import tkMessageBox

class AppMenu(Tk):
    
    '''
    Constructor
    '''
    def __init__(self, title="Aplicación con Menú"):
        Tk.__init__(self)         
        self.title(title)
        self.geometry("400x300")
        
        self.createWidgets()
    
    def createWidgets(self):   
        barramenu = Menu(self)
        
        primermenu = Menu(barramenu)
        segundomenu = Menu(barramenu)
        
        primermenu.add_command(label="Submenú 11", command=self.accion11)
        primermenu.add_command(label="Submenú 12", command=self.accion12)
        primermenu.add_separator()
        primermenu.add_command(label="Salir", command=self.salir)
        
        segundomenu.add_command(label="Submenú 21", command=self.accion11)
        segundomenu.add_command(label="Submenú 22", command=self.accion12)
        
        barramenu.add_cascade(label="Primer Menú", menu=primermenu)
        barramenu.add_cascade(label="Segundo Menú", menu=segundomenu)
        
        self.config(menu=barramenu)
     
    def accion11(self):
        self.ventanaAux = Tk()
        self.ventanaAux.geometry("200x150")
        
        self.label = Label(self.ventanaAux, text="Se ha pulsado la opción Submenú 11")
        self.label.place(x=10,y=10)
        self.ventanaAux.mainloop()
        
    def accion12(self):
        print "Se ha pulsado la opción Submenú 12"
          
    def salir(self):
        res = tkMessageBox.askquestion("Mensaje confirmación", 
                                 "¿Está seguro que desea salir")
        print res
        
        if res == 'yes':
            self.destroy()
            
app = AppMenu()
app.mainloop()    