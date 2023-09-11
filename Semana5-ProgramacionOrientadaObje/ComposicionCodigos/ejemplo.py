class Clothing:
  stock={ 'name': [], 'material': [], 'amount': []}
  def __init__(self, name):
    material = ""
    self.name = name
  def add_item(self, name, material, amount):
    Clothing.stock['name'].append(self.name)
    Clothing.stock['material'].append(self.material)
    Clothing.stock['amount'].append(amount)
  def Stock_by_Material(self, material):
    count = 0
    n = 0
    for item in Clothing.stock['material']:
      if item == material:
        count += Clothing.stock['amount'][n]
      n += 1
    return count

class shirt(Clothing):
  material="Cotton"
class pants(Clothing):
  material="Cotton"

polo = shirt("Polo")
sweatpants = pants("Sweatpants")
polo.add_item(polo.name, polo.material, 4)
sweatpants.add_item(sweatpants.name, sweatpants.material, 6)
current_stock = polo.Stock_by_Material("Cotton")
print(current_stock)


"""Este código define una estructura de clases para el seguimiento del inventario de prendas de vestir con ciertas propiedades
como nombre, material y cantidad en stock. Aquí tienes una explicación línea por línea:

1. Se define la clase `Clothing`. Esta clase tiene un diccionario llamado `stock` que se utiliza para realizar un seguimient
del inventario de prendas de vestir. El diccionario tiene tres listas: `name`, `material` y `amount`, que almacenan los
nombres de las prendas, el material de las prendas y la cantidad en stock, respectivamente.

2. En el método `__init__` de la clase `Clothing`, se inicializa una variable local `material` que no se utiliza en ningún
otro lugar del código. Además, se inicializa el atributo `name` de la instancia de la clase `Clothing` con el nombre
proporcionado al crear una instancia de la clase.

3. El método `add_item` se utiliza para agregar una prenda de vestir al inventario. Toma tres argumentos: `name`
(nombre de la prenda), `material` (material de la prenda) y `amount` (cantidad en stock). Sin embargo, hay un problema
en este método. En lugar de usar los argumentos proporcionados, está utilizando las variables `self.name` y `self.material`,
que no están definidas en el método `add_item`. Esto significa que el método siempre agregará la misma prenda al inventario,
no importa qué argumentos se le pasen.

4. El método `Stock_by_Material` toma un material como argumento y busca en el inventario para contar la cantidad total de
prendas hechas de ese material. Sin embargo, el método también tiene problemas. Al igual que en el método `add_item`, está
utilizando las variables no definidas `self.name` y `self.material`, lo que hace que no funcione correctamente.

5. Luego, se definen dos clases, `shirt` y `pants`, que heredan de la clase base `Clothing`. Estas clases establecen el
atributo de clase `material` en "Cotton". Sin embargo, esto no se utiliza en ninguna otra parte del código y no afecta el
funcionamiento del programa.

6. Se crean dos instancias de las clases `shirt` y `pants` llamadas `polo` y `sweatpants`, respectivamente. Se llama al
método `add_item` en ambas instancias para agregar 4 camisetas y 6 pantalones al inventario, pero debido a los problemas
en el método `add_item`, esto no se hace correctamente.

7. Finalmente, se llama al método `Stock_by_Material` en la instancia `polo` para contar la cantidad de prendas de "Cotton"
en el inventario y se imprime el resultado.

En resumen, el código tiene varios problemas en los métodos `add_item` y `Stock_by_Material` que impiden que funcione
correctamente para realizar un seguimiento del inventario de prendas de vestir."""
