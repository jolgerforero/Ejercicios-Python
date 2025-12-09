def capturar_datos():
    pulgadas=float(input("ingrese pulgadas"))
    return pulgadas

def procesar(pulgadas):
    centimetros= pulgadas*2.54
    return centimetros

def mostrar(centimetros):
    print("en centimetros es:",centimetros)
    
pulgadas= capturar_datos()
centimetros= procesar(pulgadas)
mostrar(centimetros)
