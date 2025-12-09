    
def area_cuadrado(lado):
    area= lado**2
    return area
lado=float(input("ingresar valor del lado: "))
resultado=area_cuadrado(lado)
print( f"el area del cuadrado es:{resultado}")