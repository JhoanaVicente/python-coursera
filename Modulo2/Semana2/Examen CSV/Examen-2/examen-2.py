"""USANDO NUEVAMENTE EL ARCHIVO CSV DE FLORES, completamos la funcion contents_of_file para procesar los datos sin convertirlos
en un diccionario. ¿Como se salta el registro del encabezado con los nombres de los campos?"""

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
        # Read the rows of the file
        rows = file.readlines()

        # Process each row (skipping the header)
        for row in rows[1:]:
            data = row.strip().split(",")  # Split the row into a list of values
            name, color, flower_type = data
            # Format the return string for data rows only
            return_string += "a {} {} is {}\n".format(color, name, flower_type)

    return return_string

# Call the function
print(contents_of_file("flowers.csv"))
