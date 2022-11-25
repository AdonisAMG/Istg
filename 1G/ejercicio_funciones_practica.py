#Escribir un algoritmo o programa en python que calcule el total
#de una factura tras aplicarle el iva. dentro del programa la function
#debe recibir la cantidad sin iva y el porcentaje de iva a aplicarse
#y debera devolver el total de la factura


def calculo_iva_factura(valor=0.0, iva=0.0):
    valor_iva = (iva)/100 * valor
    total_iva = valor + valor_iva
    return total_iva


def funcion_principal():
    valor_fact = float(input("Ingrese el valor de la factura: "))
    iva_fact = float(input("Ingrese el porcentaje del iva: "))
    v_calculo = calculo_iva_factura(valor_fact, iva_fact)
    print("El Valor con iva es : ",v_calculo)


funcion_principal()