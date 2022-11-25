print("Ejercicio del semaforo puede ingresar los colores (amarillo/rojo/verde)")
color = input("Ingrese el color : ")
if  color.lower() == "amarillo":
    print("Alto no puede cruzar la calle")
elif color.lower() == "rojo":
    print("Detengase no puede cruzar la calle ")
elif color.lower() == "verde":
    print("Puede cruzar la calle")
else:
    print("Dato no valido para el semaforo")