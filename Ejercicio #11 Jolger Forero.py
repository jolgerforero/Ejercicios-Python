def capturar_datos_11():
    print("Capturando datos...")
    km = float(input("Ingrese los kilómetros:"))
    print(f"Kilómetros recibidos: {km}")
    return km
def procesar_11(km):
    millas = km * 0.621371
    return millas
def mostrar_11(millas):
    print("\n" + "-"*40)
    print(f"Las millas son: {millas}")
    print("-"*40)
print("="*50)
print("="*50)
print()
km = capturar_datos_11()
print(f"\nValor capturado: km={km}")
millas = procesar_11(km)
mostrar_11(millas)
print("\n✅ Programa finalizado correctamente")