'''
Created on 2 nov. 2017

@author: 21650521
'''
mi_diccionario = {'Puertas': 4, 'Ventanas': 8,'Asientos': '5 asientos'}
print mi_diccionario['Puertas'] # Salida: 4
#Un diccionario permite eliminar cualquier entrada:

del(mi_diccionario['Ventanas'])
#Al igual que las listas, el diccionario permite modificar los valores

print mi_diccionario['Asientos']

#Agrego a mi diccionario la clave Motor y le doy un valor de 110CV
mi_diccionario['Motor'] = '110CV'

print mi_diccionario['Motor']