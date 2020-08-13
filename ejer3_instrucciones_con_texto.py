mi_cadena= "Hola mundo!"
mi_cadena2= 'Hola mundo!'

print(mi_cadena)

#Si se va a mostrar comillas en una cadena, se debe poner una comilla contraria a las que se va a utilizar

cadena_con_comillas= 'Javier dijo: "Hola Mundo"'
print(cadena_con_comillas)

comillas_simples= "Hello it's me!"
print(comillas_simples)


#EL \ INDICA QUE LAS "" QUE ESTAN DENTRO DE LA CADENA, PERTENECEN AL TEXTO
cadena_con_comillas= "Javier dijo: \"Hola Mundo!\""
print(cadena_con_comillas)
#A esto se le llama escapar y en python es usado para remover, en este caso eliminar el significado de las comillas

#Para hacer esto se pone 3 " al principio y 3 " al final para armar el texto multilinea
multilinea=""" Hola bienvenido.

Actualmente estás en el curso de Python
"""
print(multilinea)

nombre= "Luis"
saludo= " Buenos días "

union_cadena= nombre + saludo
print(union_cadena)

edad= 21
#Convierte en cadena cualquier valor
numero_con_cadena= str(edad)
print("Tu edad es: " + numero_con_cadena)