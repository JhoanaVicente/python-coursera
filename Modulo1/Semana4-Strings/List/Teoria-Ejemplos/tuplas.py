def convert_seconds(seconds):
    hours = seconds // 3600
    minutes = (seconds - hours * 3600) // 60
    remaining_seconds = seconds - hours * 3600 - minutes * 60
    return hours, minutes, remaining_seconds

result = convert_seconds(5000)
type(result)
print(result)

#Dividimos la tupla en 3 valores separados:
hours, minutes, seconds = result
print(hours, minutes, seconds)

#Tambien podemos llamar a la funcion sin la variable de resultado inmediato:
hours, minutes, seconds = convert_seconds(1000)
print(hours, minutes, seconds) #En Python usamos tuplas para representar datos

"""Example:
En este código, utilizamos una tupla file_info para almacenar información sobre el archivo, donde el primer elemento es el
nombre, el segundo es el tipo y el tercer elemento es el tamaño en bytes. Luego, extraemos el tercer elemento de la tupla
(el tamaño) y dividimos entre 1024 para convertirlo en kilobytes. Finalmente, utilizamos el método .format() para dar formato
al resultado con dos decimales y lo devolvemos como una cadena."""

def file_size(file_info):
	name, file, size= file_info
	return("{:.2f}".format(size / 1024))

print(file_size(('Class Assignment', 'docx', 17875))) # Should print 17.46
print(file_size(('Notes', 'txt', 496))) # Should print 0.48
print(file_size(('Program', 'py', 1239))) # Should print 1.21

