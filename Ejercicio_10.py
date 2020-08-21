# El programa tiene que pedir la nota de 15 alumnos y sacar por pantalla cuantos han aprobado
# y cuantos han suspendido.

aprobados=0
reprobados=0

for numero in range(1, 16):

    nota=(float(input("Escriba la nota: ")))

    if(nota>=3 and nota<=5):
        print("El estudiante aprobó")
        aprobados=aprobados+1
    else:
        print("El estudiante reprobó")
        reprobados=reprobados+1

    print(" ")

print(f"El numero de estudiante arpobados es: {aprobados}")
print(f"El numero de estudiantes reprobados es: {reprobados}") 