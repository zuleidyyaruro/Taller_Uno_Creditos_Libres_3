# Hacer un programa que muestre todos los numeros entre dos numeros que diga el usuario.

numero_1=int(input("Indica el primer numero"))
numero_2=int(input("Indica el segundo numero"))

for numero in range (numero_1, (numero_2+1)):
    print(numero)