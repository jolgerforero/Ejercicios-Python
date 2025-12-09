def capturar_datos():
    numero1=float(input("digite el numero1"))
    numero2=float(input("digite el numero2"))
    return numero1,numero2

def procesar(numero1,numero2):
    division=numero1 / numero2
    return division

def mostrar(division):
  print("el valor del division es:",division)

numero1,numero2= capturar_datos()
division= procesar(numero1,numero2)
mostrar (division)