producto1= "Cereal"
producto2= "Leche"
producto3= "Pan"

print(producto1)
productos= ["Cereal", "Leche", "Pan", "Jugo"]
numeros= [1,2,3,4]
listas_cosas= ["Manzana",1,3.1416, "Luis"]

print(productos[1])
print(listas_cosas[2])
print(len(productos))


#Listas de Listas
mejores_amigos=[["Diego", 18], ["Nathaly", 21], ["Miguel", 25]]

#Listas Anidadas
print(mejores_amigos[1][0])
print(mejores_amigos[2][1])

productos.append("Arroz")
print(productos)
mejores_amigos.append(["Juan",24])
print(mejores_amigos)

productos.remove("Pan")
print(productos)