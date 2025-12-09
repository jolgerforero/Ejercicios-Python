def capturar_datos():
    numero1=float(input("digite el numero1"))
    numero2=float(input("digite el numero2"))
    return numero1,numero2

def procesar(numero1,numero2):
    producto=numero1 * numero2
    return producto

def mostrar(producto):
  print("el valor del producto es:",producto)

numero1,numero2= capturar_datos()
producto= procesar(numero1,numero2)
mostrar (producto)