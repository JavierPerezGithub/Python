from Tkinter import *


class Application(Tk):
    def __init__(self):
        
        Tk.__init__(self)
        self.title("Viajes de senderismo")
        self.geometry("1500x900")
        self.configure(background='dark turquoise')
        self.createWidgets()
        
    def createWidgets(self):
        label_titulo = Label(self, font="Courier 36 bold", bg = "dark turquoise",  text = "Viajes de Senderismo").place(x=10, y=10)
        opcion = StringVar()
        opcion1 = Radiobutton(self, text = "Excursion 1", font = "Courier 16 bold", bg = "dark turquoise",   value = "excursion1", variable = opcion).place(x=10, y =100)
        opcion2 = Radiobutton(self, text = "Excursion 2", font = "Courier 16 bold", bg = "dark turquoise", value = "excursion2", variable = opcion).place(x=250, y = 100)
        opcion3 = Radiobutton(self, text = "Excursion 3", font = "Courier 16 bold", bg = "dark turquoise", value = "excursion3", variable = opcion).place(x=490, y = 100)
        
        checkvar1 = StringVar()
        checkvar2 = StringVar()
        checkvar3 = StringVar()
        
        check1 = Checkbutton(self, text ="Linterna", font = "Courier 16 bold", bg = "dark turquoise", variable = checkvar1, onvalue = "linterna", offvalue="").place(x=10, y=200)
        check2 = Checkbutton(self, text ="GPS", font = "Courier 16 bold", bg = "dark turquoise", variable = checkvar2, onvalue = "gps", offvalue="").place(x=250, y=200)
        check3 = Checkbutton(self, text ="Mapa", font = "Courier 16 bold", bg = "dark turquoise", variable = checkvar3, onvalue = "mapa", offvalue="").place(x=490, y=200)
        
        label_nombre = Label(self, text="Nombre").place(x=10, y=300)
        sNombre = StringVar()
        caja_nombre = Entry(self, textvariable=sNombre, width="20").place(x=250, y=300)

        label_apellidos = Label(self, text="Apellidos").place(x=10, y=360)
        sApellidos = StringVar()
        caja_apellidos = Entry(self, textvariable=sApellidos, width="40").place(x=250, y=360)

        
        
        
        


app = Application()
app.mainloop()
    