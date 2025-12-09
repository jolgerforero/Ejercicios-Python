def capturar_datos():
    base=float(input("digite el numero1"))
    altura=float(input("digite el numero2"))
    return base,altura

def procesar(base,altura):
    area= base * altura
    return area

def mostrar(area):
  print("el area del triangulo es:",area)

base,altura= capturar_datos()
area= procesar(base,altura)
mostrar (area)