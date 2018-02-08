'''
Created on 2 nov. 2017

@author: 21650521
'''
mi_lista = ['cadena de texto', 15, 2.8, 'otro dato', 25]
# A las listas se accede igual que a las tuplas, por su numero de indice:
print mi_lista[1] # Salida: 15

print mi_lista[1:4] # Devuelve: [15, 2.8, 'otro dato']

print mi_lista[-2] # Salida: otro dato

mi_lista[2] = 3.8 # el tercer elemento ahora es 3.8

mi_lista.append("Nuevo") #Agrego un dato a la lista

print mi_lista[-1]

#mostrar valores en mi_lista

for i in mi_lista:
    print i