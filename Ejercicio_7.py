# Hacer un programa que muestre todos los números impares entre dos números que decida el
# usuario.

numero_1=int(input("Ingrese el primer número: "))
numero_2=int(input("Ingrese el segundo número: "))

for numero in range (numero_1, (numero_2+1)):
    if(numero%2 != 0):
        print(numero)