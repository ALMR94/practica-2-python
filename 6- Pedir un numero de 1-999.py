# -*- coding: cp1252 -*-
print "Dime un número de como máximo 3 cifras:"
a= int(raw_input())
if a<1000 and a>0:
    print "El número",a,"es válido."
else:
    print "El número introducido no es válido o no es de 3 cifras."
