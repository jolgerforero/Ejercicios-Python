def capturar_datos():
    numero1=float(input("digite el numero1"))
    numero2=float(input("digite el numero2"))
    return numero1,numero2

def procesar(numero1,numero2):
    residuo=numero1 / numero2
    return residuo

def mostrar(residuo):
  print("el residuo es:",residuo)

numero1,numero2= capturar_datos()
residuo= procesar(numero1,numero2)
mostrar (residuo)