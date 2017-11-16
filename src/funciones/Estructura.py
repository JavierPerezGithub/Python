'''
Created on 16 nov. 2017

@author: 21650521
'''
def mi_funcion():
    print "Hola mundo"
mi_funcion()

def saludar(nombre, mensaje='Hola'):
    print mensaje, nombre
    # Imprime: Hola Andres
saludar('Paco')

def calcular(importe, descuento):
    return importe - (importe * descuento / 100)

datos = {'descuento': 10, 'importe':1500}
print calcular(**datos)