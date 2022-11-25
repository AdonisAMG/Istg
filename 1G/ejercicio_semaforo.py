print("Ejercicio del Semaforo")
dato = input("Ingrese el color del semaforo: ")
if dato.lower() == "amarillo":
    print("No puede cruzar la calle")
elif dato.lower() == "rojo":
    print("Alto no puede cruzar la calle")
elif dato.lower() == "verde":
    print("Puede cruzar la calle")
else:
    print("Valor o informacion no valida para el semaforo")