import os

list_bodega1 = []
list_bodega2 = []
sw = True

def fnt_registrar():
    os.system("cls")
    año = input("Ingrese el año del vehiculo: ")
    modelo = input("Ingrese el modelo del vehiculo: ")
    motor = input("Ingrese el numero de motor")
    fabricante = input("1. Chevrolet\n2. Ford\n3. Renault\n4. Dodge\n5. Hyunda\n6. Fiat\n ->")
    if año == '2024' and (fabricante == "1" or fabricante == "2" or fabricante == "3")
        list_bodega1.append([año, modelo, motor, fabricante])
        enter = input("Vehiculo registrado con exito <ENTER>")

while sw == True:
    os.system("cls")

    opcion = input("1. Registrar\n2. Mostrar")
    if opcion == "1":
        fnt_registrar()
