def capturar_datos():
    numero1=float(input("digite el numero1"))
    numero2=float(input("digite el numero2"))
    return numero1,numero2

def procesar(numero1,numero2):
    suma= (numero1 + numero2)
    return suma

def mostrar(suma):
    print("el valor de suma es:",suma)

numero1,numero2= capturar_datos()
suma= procesar(numero1,numero2)
mostrar (suma)