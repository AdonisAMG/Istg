print("Ejercicio Lista de Supermercado")
lista = []
while True:
   dato = input("Ingrese el Producto: ")

   lista.append(dato)

   print(lista)

   opcion = input("Desea Continuar s/n : ")

   if (opcion.lower() == 's'):
      continue
   else:
       break

