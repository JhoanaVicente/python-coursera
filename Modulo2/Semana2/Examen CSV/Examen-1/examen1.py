"""ESTAMOS TRABAJANDO CON UNA LISTA DE FLORES Y ALGO DE INFORMACION SOBRE CADA UNA. La funcion create_file escribe esta
informacion en un archivo CSV. La funcion content_of_file lee este archivo en resgistros y devuelve la informacion en
un bloque bien formateado. Se completa la funcion content_of_file para convertir
los datos del archivo CSV en un diccionario usando DictReader."""

import csv

# Create a file with data in it
def create_file(filename):
    with open(filename, "w") as file:
        file.write("name,color,type\n")
        file.write("carnation,pink,annual\n")
        file.write("daffodil,yellow,perennial\n")
        file.write("iris,blue,perennial\n")
        file.write("poinsettia,red,perennial\n")
        file.write("sunflower,yellow,annual\n")

# Read the file contents and format the information about each row
def contents_of_file(filename):
    return_string = ""

    # Call the function to create the file
    create_file(filename)

    # Open the file
    with open(filename, "r") as file:
        # Create a CSV reader object
        csv_reader = csv.DictReader(file)

        # Process each row in the CSV file
        for row in csv_reader:
            return_string += "a {} {} is {}\n".format(row["color"], row["name"], row["type"])
    return return_string

# Call the function
print(contents_of_file("flowers.csv"))


"""Esta función, llamada `contents_of_file`, se encarga de realizar las siguientes acciones:

1. Crea un archivo CSV llamado "flowers.csv" y escribe datos en él. Estos datos representan información sobre flores,
incluyendo el nombre, el color y el tipo de cada flor.

2. Luego de crear el archivo, abre ese archivo y comienza a leer su contenido.

3. Utiliza el módulo `csv` de Python para facilitar la lectura del archivo CSV. Este módulo permite trabajar con archivos
CSV de una manera más sencilla.

4. A medida que lee cada fila del archivo CSV, extrae la información de las columnas "color," "name" y "type" de cada fila.

5. Luego, formatea esta información en una cadena de texto en un formato específico. Por ejemplo, para una flor, la cadena
generada se verá como "una flor de color [color] se llama [nombre] y es de tipo [tipo]."

6. Finalmente, todas estas cadenas generadas se concatenan en una única cadena llamada `return_string`, que contiene la
información formateada de todas las flores en el archivo CSV.

7. La función devuelve esta cadena `return_string`, que contiene toda la información de las flores en el archivo CSV, cada
una en su formato correspondiente.

8. Finalmente, esta cadena se imprime en la consola cuando se llama a la función `contents_of_file("flowers.csv")`.

En resumen, esta función crea un archivo CSV con datos de flores, lo lee, formatea la información de las flores y devuelve
una cadena con la información de todas las flores en un formato específico."""
