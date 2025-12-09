def capturar_datos():
    base = float(input("Ingrese la base: "))
    altura = float(input("Ingrese la altura: "))
    return base, altura
def procesar(base, altura):
    area = base * altura
    return area
def mostrar(area):
    print(f"El área del paralelogramo es: {area}")
    print("\n" + "="*50)
    print("="*50)
  
base, altura = capturar_datos()
area = procesar(base, altura)
mostrar(area)