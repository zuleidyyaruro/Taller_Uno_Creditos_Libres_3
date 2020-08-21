# Hacer un programa que pida numeros al usuario indefinidamente hasta meter el numero 111

num=int(input("Ingresar numero: "))

while num:
    num=int(input("Ingresar numero: "))
    if num==111:
        break
