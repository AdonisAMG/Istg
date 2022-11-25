#Ejercicio 1
#Bienvenido a la calculadora

while True:
    opcion = "problemas matematicos"
    print("Bienvenido a tu calculadora")
    print("1_Multiplicacion")
    print("2_Division")
    print("3_Sumar")
    opcion =input("Ingrese una opcion: ")
    print()
    if (opcion== "1"):
        n1=int(input("Ingrese el primer numero: "))
        n2=int(input("Ingrese el segundo numero: "))
        total= n1*n2
        print("La multiplicacion de los dos numeros es:", total)
        print()
    elif (opcion== "2"):
        n1=int(input("Ingrese el primer numero: "))
        n2=int(input("Ingrese el segundo numero: "))
        total= n1/n2
        print("La division de los dos numeros es:", total)
        print()
    elif (opcion== "3"):
        n1=int(input("Ingrese el primer numero: "))
        n2=int(input("Ingrese el segundo numero: "))
        total= n1+n2
        print("La division de los dos numeros es:", total)
        print()
    else:
        print("Ojalá te haya gustado nuestro servicio")
        break