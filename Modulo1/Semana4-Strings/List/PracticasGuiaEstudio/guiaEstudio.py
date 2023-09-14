"""Utilice un bucle for para modificar elementos de una lista.
Utilice el método list.append(antiguo,nuevo) .
Utilice los métodos string.endswith() y string.replace() para modificar los elementos dentro de una lista."""

years = ["January 2023", "May 2025", "April 2023", "August 2024", "September 2025", "December 2023"]
updated_years = []

for year in years:
    if year.endswith("2023"):
        new = year.replace("2023", "2024")
        updated_years.append(new)
    else:
        updated_years.append(year)
print(updated_years)
# Should print ["January 2024", "May 2025", "April 2024", "August 2024", "September 2025", "December 2024"]

"""Utilice el método string[index] dentro de una lista por comprensión.
Utilice una lista por comprensión para modificar elementos de una lista.
Utilice el método string.replace() dentro de una lista por comprensión."""

years = ["January 2023", "May 2025", "April 2023", "August 2024", "September 2025", "December 2023"]
updated_years = [year.replace("2023", "2024") if year[-4:] == "2023" else year for year in years]

print(updated_years)
# Should print ["January 2024", "May 2025", "April 2024", "August 2024", "September 2025", "December 2024"]

"""Este código actualiza los años en las fechas que contienen "2023" en la lista years y luego imprime la lista
actualizada updated_years."""

