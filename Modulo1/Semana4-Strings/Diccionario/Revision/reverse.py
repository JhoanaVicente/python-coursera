def record_profit_years(recent_first, recent_last):
    recent_first.reverse()
    recent_last.extend(recent_first)
    return recent_last

recent_first = [2022, 2018, 2011, 2006]
recent_last = [1989, 1992, 1997, 2001]

# Call the record_profit_years() function and pass the two lists as
# parameters.
print(record_profit_years(recent_first, recent_last))
# Should print [1989, 1992, 1997, 2001, 2006, 2011, 2018, 2022]


"""recent_first.reverse(): Esto invierte el orden de los elementos en la lista recent_first. Como resultado, la lista recent_first quedará como [2006, 2011, 2018, 2022].

recent_last.extend(recent_first): Esto agrega todos los elementos de la lista recent_first al final de la lista recent_last.
Después de esta línea, la lista recent_last contendrá todos los elementos de ambas listas en el orden en que se ejecutaron
las operaciones. En este caso, recent_last quedará como [1989, 1992, 1997, 2001, 2006, 2011, 2018, 2022].

Finalmente, la función devuelve la lista recent_last, que contiene los elementos de ambas listas en el orden deseado.

Se llama a la función record_profit_years con las listas recent_first y recent_last como argumentos, y el resultado se imprime utilizando print().

La salida esperada es [1989, 1992, 1997, 2001, 2006, 2011, 2018, 2022], que es el resultado de combinar las dos listas
con el orden especificado después de las operaciones realizadas en la función."""
