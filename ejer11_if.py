productos_descuento= ["Computadora", "Televisión","Teclado","Mouse","Cartera","Monitor"]

sin_stock=["Cámara", "Celular", "Reloj","Memoria"]
producto= input("Ingresa un producto: ")
if producto in productos_descuento:
  print("Este producto si está en descuento")
  print("Aprovecha la oferta!")
elif producto in sin_stock:
  print("Este producto se encuentra agotado")
else:
  print("Lo sentimos, este producto no está en oferta")
print("Fin de la Sentencia if")