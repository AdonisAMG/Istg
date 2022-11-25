
def ordenamientoBurbuja(unaLista):
    for numPasada in range(1, len(unaLista)):
        for i in range(0, len(unaLista)-1):
            print("A", unaLista[i], ">", unaLista[i + 1])
            if unaLista[i]>unaLista[i+1]:
                print("D", unaLista[i], ">", unaLista[i + 1])
                temp = unaLista[i]
                unaLista[i] = unaLista[i+1]
                unaLista[i+1] = temp
                print("nueva lista -->", unaLista)

def funcion_principal():
    # El siguiente arreglo o lista inicial
    # [66, 22, 83, 50, 79, 87, 49, 58, 21, 19, 109, 33]
    unaLista = [81, 67, 54, 44, 33, 27, 26, 25, 20]
    print("Lista Inicial -> ", unaLista)
    ordenamientoBurbuja(unaLista)

    #print(unaLista)

funcion_principal()
