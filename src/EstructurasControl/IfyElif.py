'''
Created on 2 nov. 2017

@author: 21650521
'''
semaforo = 'rojo'
compra =20

if semaforo == 'verde':
    print "Cruzar la calle"
elif semaforo == 'amarillo':
    print "Mucho cuidado"
elif semaforo == 'rojo':
    print "Ni se te ocurra cruzar"
else:
    print "Cruza cuando no veas coches porque no funciona el semaforo"  
    
if compra <= 100:
    print "Pago en efectivo"
elif compra> 100 and compra< 300:
    print "Pago con tarjeta de debito"
else:
    print "Pago con tarjeta de credito"
