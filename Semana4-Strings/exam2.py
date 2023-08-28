"""Desglose de la función:
km = miles * 1.6: Calcula la distancia en kilómetros multiplicando la cantidad de millas por el factor de conversión
(1 milla equivale a aproximadamente 1.6 kilómetros).

result = "{} miles equals {:.1f} km".format(miles, km): Crea la cadena de resultado utilizando el método format para incorporar
los valores de miles y km en la cadena. La parte {:.1f} en la cadena de formato asegura que el valor de km se muestre con un decimal.

return result: Devuelve la cadena formateada que muestra la cantidad de millas y su equivalente en kilómetros con un decimal.

Los ejemplos print(convert_distance(...)) al final llaman a la función con diferentes cantidades de millas y muestran los
resultados formateados según lo descrito anteriormente.

En resumen, la función convierte la cantidad de millas dada en su equivalente en kilómetros, y luego crea una cadena que
muestra ambas cantidades con formato adecuado."""

def convert_distance(miles):
    km = miles * 1.6
    result = "{} miles equals {:.1f} km".format(miles, km)
    return result

print(convert_distance(12)) # Should be: 12 miles equals 19.2 km
print(convert_distance(5.5)) # Should be: 5.5 miles equals 8.8 km
print(convert_distance(11)) # Should be: 11 miles equals 17.6 km
