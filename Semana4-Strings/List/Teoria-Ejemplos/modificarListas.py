fruits = ["Piña", "Plátano", "Manzana", "Melón"]
fruits.append("Kiwi") #Agrega elementos al final de la lista
print(fruits)

fruits.insert(0, "Orange") #Agregar elementos en una posicion especifica
print(fruits)

fruits.insert(25, "Melocoton")
print(fruits)

fruits.remove("Melón") #Elimina lo que hay en la lista
print(fruits)

fruits.pop(3) #Elimina un parametro especifico
print(fruits)

fruits[2] = "Fresa" #Indexacion para sobreescribir el valor almacenado en el indice especificado
print(fruits)
