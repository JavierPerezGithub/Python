from Tkinter import *
ventana1 = Tk()

boton = Button(ventana1, text="Minimizar", command=ventana1.iconify)
boton.pack()
ventana1.mainloop()