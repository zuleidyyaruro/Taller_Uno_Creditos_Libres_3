#Escribir un programa que muestre los cuadrados(un numero multiplicado por si mismo) de los
#60 primeros números naturales. Resolverlo con for y con while

for numero in range(1, 61):
    numero=numero*numero
    print (f"El cuadrado de {numero} es {numero}")


print ("----------------------------")
contador=1


while contador<=60:
    a=contador*contador 
    print (f"El cuadrado de {contador} es {a}")
    contador= contador + 1

