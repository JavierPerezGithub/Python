# -*- coding: utf-8 -*-
'''
Created on 6 feb. 2017

@author: profesoresi
'''
from Tkinter import Tk, Button

class Application(Tk):     
    
    def __init__(self):         
        Tk.__init__(self)         
        self.title("Ventana Python")
        self.geometry("200x100")
        
        self.createWidgets()

    def createWidgets(self):         
        self.hola = Button(self)         
        self.hola["text"] = "SALUDAR"         
        self.hola["command"] = self.di_hola         
        self.hola.place(x=10, y=10) 
 
        self.salir = Button(self, text="SALIR", fg="red", command=self.destroy)         
        self.salir.place(x=90, y=10)

    def di_hola(self):         
        print "Hola a todos, DAM ALCOBENDAS!" 

app = Application()
app.mainloop()
