while True:
   print("Hola Carapaz ")
   opcion = input("desea continuar S/N: ")
   if opcion.lower() == "s":
      continue
   elif opcion.lower() == "n":
      break
   else:
      print("dato no valido")
      break