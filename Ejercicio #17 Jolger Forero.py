def capturar_datos():
    libras=float(input("ingrese libras"))
    return libras

def procesar(libras):
    kilogramos=libras*0.45
    return kilogramos

def mostrar(kilogramos):
    print("en kilogramos es:",kilogramos)

libras=capturar_datos()
kilogramos=procesar(libras)
mostrar(kilogramos)