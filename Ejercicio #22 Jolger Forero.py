def capturar_datos():
    numero1=float(input("digite el numero1"))
    numero2=float(input("digite el numero2"))
    return numero1,numero2

def procesar(numero1,numero2):
    resta= (numero1 - numero2)
    return resta

def mostrar(resta):
    print("el valor de resta es:",resta)

numero1,numero2= capturar_datos()
resta= procesar(numero1,numero2)
mostrar (resta)