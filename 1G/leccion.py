print("Ejercicio que valida valores")
dato = float(input("Ingrese un valor : "))
if dato <100:
    print("El valor es pequeño")
elif dato >= 100 and dato < 500:
    print("El valor es mediano")
else:
    print("El valor es alto")