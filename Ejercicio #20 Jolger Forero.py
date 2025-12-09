def capturar_datos():
   litros = float(input("ingrese litros"))
   return litros

def procesar(litros):
    galones = litros * 2.54
    return galones

def mostrar(galones):
    print("en galones es:", galones)

litros = capturar_datos()  
galones = procesar(litros)
mostrar(litros)