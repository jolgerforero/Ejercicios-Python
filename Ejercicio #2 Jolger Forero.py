#***********************funciones***************************
def definir_pi():
    pi= 3.1416
    return pi

def sacar_radio():
    radio=20
    return radio

def calcule_volumen(pi, radio):
   volumen= (radio** 3 * pi) * 4/3
   return volumen

def imprimir_mensaje(volumen):
    mensaje= "el volumen de una esfera es:" +  str(volumen)
    return mensaje

def dar_mensaje(mensaje):
    print(mensaje)


#***************************zona de codigo principal******************************

print("volumen de un circulo \n")
pi = definir_pi
radio=sacar_radio
circulo= calcule_volumen(pi,radio)
mensaje=imprimir_mensaje(circulo)
dar=dar_mensaje(mensaje)
