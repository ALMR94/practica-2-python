# -*- coding: cp1252 -*-
print "Dime un n�mero de como m�ximo 3 cifras:"
a= int(raw_input())
if a<1000 and a>0:
    print "El n�mero",a,"es v�lido."
else:
    print "El n�mero introducido no es v�lido o no es de 3 cifras."
