print("vocales")
datos = input("vocal : ")
if datos.upper() == "a" or datos.upper() == "e" or datos.upper() == "o":
    print("abiertas")
elif datos.lower() == "i" or datos.lower() == "u":
    print("cerradas")
else:
    print("nada")