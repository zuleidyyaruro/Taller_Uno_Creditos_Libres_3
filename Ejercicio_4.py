# Pedir dos numeros al usuario y hacer todas las operaciones básicas de una calculadora y
# mostrarlo por pantalla.

print(" ")
x=float(input("Indica el valor de x: "))
y=float(input("Indica el valor de y: "))

print(" ")
print("+++++ OPERACIONES MATEMÁTICAS +++++")
print(" ")
print("1. Sumar")
print("2. Restar")
print("3. Multiplicar")
print("4. Dividir")


print(" ")
opcion=int(input("Escoja una Opción:  "))
print(" ")

if opcion==1:
    resultado=x+y
    print(x , " + " , y , " = " , resultado)
elif opcion==2:
    resultado=x-y
    print(x , " - " , y , " = " , resultado)
elif opcion==3:
    resultado=x*y
    print(x , " * " , y , " = " , resultado)
elif opcion==4:
    resultado=x/y
    print(x , " / " , y , " = " , resultado)
