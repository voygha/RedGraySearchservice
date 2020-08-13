productos= 21
caja_rapida= productos <= 10
caja_autocobro= productos < 26
print(caja_rapida)
print(caja_autocobro)
#Uso de comparacion sin el if 
#pregunta si son 20 productos
veinte_productos = productos == 20
print(veinte_productos)

numero_ganador=23
numero_cliente= int(input("Ingresa un número para adivinar: "))
print(numero_ganador == numero_cliente)
