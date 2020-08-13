carrito_compras= []
agregar_producto = input(" ¿Quieres agregar un producto a tu carrito? ( si/no ):  ")


while agregar_producto == "si":
  nuevo_producto =input("Ingresa el producto: ")
  carrito_compras.append(nuevo_producto)
  agregar_producto = input("¿Deseas Agragar Otro Producto? ( si/no ): ")

print(carrito_compras)