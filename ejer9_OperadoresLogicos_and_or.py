edad_cliente= int(input("Ingresa tu edad: "))
tarjeta_credito= edad_cliente >= 18 and edad_cliente <= 70 
print("Puedes tener tu tarjeta de crédito: ", tarjeta_credito)

descuento = edad_cliente == 20 or edad_cliente == 30
print("Puedes obtener el descuento: ", descuento)

cadena= input("Ingresa una Palabra: ")
resultado_cadena= len(cadena) > 5 or cadena[2] == "h"
print(resultado_cadena)