#Elaborar un programa en python con el empelo de funciones que me permita
#el ingreso del valor de la factura y que dependiendo del valor me genere
#el descuento. si la factura es menor a 100 dolares se hace el descuento de 5%
#si el valor es mayor igual a 100 y menor a 300 se debe aplicar el descuento
#del 8% y si el valor de la factura es mayor o igual 300 se debe aplicar el
#descuento del 10%


def funcion_meror_a_100(valor=0.0):
    descuento = 5/100 * valor
    total1 = valor - descuento
    return total1

def funcion_mayor_o_igual_a_100_y_menor_a_300(valor=0.0):
    descuento = 8/100 * valor
    total2 = valor - descuento
    return total2

def funcion_mayor_o_igual_a_300(valor=0.0):
    descuento = 10/100 * valor
    total3 = valor - descuento
    return total3


def funcion_principal():
    dato = float(input("Ingrese un valor : "))
    print("  ↓ ↓ ↓ ↓ ↓ ↓ ↓ ↓ ↓ ↓ ↓ ↓ ↓ ↓ ↓ ↓ ↓ ↓ ↓ ↓ ↓ ↓ ↓")
    if dato <100:
        valor_fact = dato
        v_calculo = funcion_meror_a_100(valor_fact)
        print("→ El Valor con el descuento del 5% es : ", v_calculo,"←")

    elif dato >= 100 and dato < 300:
        valor_fact = dato
        v_calculo = funcion_mayor_o_igual_a_100_y_menor_a_300(valor_fact)
        print("→ El Valor con el descuento del 8% es : ", v_calculo,"←")

    elif dato >= 300:
        valor_fact = dato
        v_calculo = funcion_mayor_o_igual_a_300(valor_fact)
        print("→ El Valor con el descuento del 10% es : ", v_calculo,"←")
    print("  ↑ ↑ ↑ ↑ ↑ ↑ ↑ ↑ ↑ ↑ ↑ ↑ ↑ ↑ ↑ ↑ ↑ ↑ ↑ ↑ ↑ ↑ ↑")
funcion_principal()
