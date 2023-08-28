""" Utilice el método format() , con {} marcadores de posición para datos variables, para crear una nueva cadena.
Utilice una expresión de formato, como {:.2f} , para formatear una variable flotante y configurar el número de
decimales que se mostrarán para la variable flotante.


La función `convert_weight` convierte una cantidad de onzas a su equivalente en libras y luego formatea el resultado
en una cadena que muestra ambas medidas. Aquí está el desglose de la función:

1. `def convert_weight(ounces):`: Define la función `convert_weight` que toma un argumento `ounces`, que representa la cantidad de onzas que se desea convertir.

2. `pounds = ounces/16`: Calcula el equivalente en libras dividiendo la cantidad de onzas por 16 (ya que hay 16 onzas en una libra).
El resultado se almacena en la variable `pounds`.

3. `result = "{} ounces equals {:.2f} pounds".format(ounces, pounds)`: Crea una cadena de resultado utilizando el método
`format` para incorporar los valores de `ounces` y `pounds` en la cadena. La parte `{:.2f}` en la cadena de formato asegura
que el valor de `pounds` se muestre con dos decimales.

4. `return result`: Devuelve la cadena formateada que muestra la cantidad de onzas y su equivalente en libras.

5. Los tres ejemplos `print(convert_weight(...))` al final llaman a la función con diferentes cantidades de onzas y muestran
los resultados formateados según lo descrito anteriormente.

En resumen, la función convierte la cantidad de onzas dada en su equivalente en libras, y luego crea una cadena que muestra ambas cantidades con formato adecuado."""

def convert_weight(ounces):
    pounds = ounces/16
    result = "{} ounces equals {:.2f} pounds".format(ounces,pounds)
    return result

print(convert_weight(12)) # Should be: 12 ounces equals 0.75 pounds
print(convert_weight(50.5)) # Should be: 50.5 ounces equals 3.16 pounds
print(convert_weight(16)) # Should be: 16 ounces equals 1.00 pounds
