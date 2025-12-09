def capturar_datos():
    numero=float(input("digite el numero"))
    return numero

def procesar(numero):
    cuadrado=numero*numero
    return cuadrado

def mostrar(cuadrado):
    print("el valor de cuadrado:",cuadrado)

numero= capturar_datos()
cuadrado= procesar(numero)
mostrar (cuadrado)