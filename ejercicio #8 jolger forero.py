def capturar_datos():
    dolares = float(input("Ingrese la cantidad de dólares: "))
    return dolares

def procesar_conversion(dolares):
    tasa = 0.92  
    euros = dolares * tasa
    return euros

def imprimir_resultado(euros):
    print(f"El equivalente en euros es: {euros:.2f} €")

# Programa principal
dolares = capturar_datos()
euros = procesar_conversion(dolares)
imprimir_resultado(euros)