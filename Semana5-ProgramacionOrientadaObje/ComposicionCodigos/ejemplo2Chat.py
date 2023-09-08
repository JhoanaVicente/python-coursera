class Clothing:
    stock = {'name': [], 'material': [], 'amount': []}

    def __init__(self, name, material):
        self.material = material
        self.name = name

    def add_item(self, name, material, amount):
        Clothing.stock['name'].append(name)
        Clothing.stock['material'].append(material)
        Clothing.stock['amount'].append(amount)

    def Stock_by_Material(self, material):
        count = 0
        n = 0
        for mat in Clothing.stock['material']:
            if mat == material:
                count += Clothing.stock['amount'][n]
            n += 1
        return count

class shirt(Clothing):
    def __init__(self, name):
        super().__init__(name, "Cotton")

class pants(Clothing):
    def __init__(self, name):
        super().__init__(name, "Cotton")

polo = shirt("Polo")
sweatpants = pants("Sweatpants")
polo.add_item(polo.name, polo.material, 4)
sweatpants.add_item(sweatpants.name, sweatpants.material, 6)
current_stock = polo.Stock_by_Material("Cotton")
print(current_stock)


"""En este código corregido:
Dentro de la clase Clothing, hemos modificado el constructor __init__ para que acepte el nombre y el material como argumentos
y los inicialice correctamente. En el método add_item, hemos modificado las líneas para que se agreguen los valores correctos
al diccionario Clothing.stock utilizando los argumentos proporcionados al llamar a add_item.
En las clases shirt y pants, hemos añadido un constructor __init__ que llama al constructor de la clase base Clothing y
pasa el nombre y el material correspondientes.
Con estas correcciones, el código debería funcionar correctamente y devolver 10 como resultado cuando se llama a polo.Stock_by_Material("Cotton")."""
