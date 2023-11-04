import datetime
from datetime import date

def add_year(date_obj):
  try:
    new_date_obj = date_obj.replace(year = date_obj.year + 1)
  except ValueError:
    # This gets executed when the above method fails,
    # which means that we're making a Leap Year calculation
    new_date_obj = date_obj.replace(year = date_obj.year + 4)
  return new_date_obj

"""La función add_year recibe un objeto de fecha (date_obj) como argumento. Intenta agregar un año al año de date_obj
utilizando el método replace. Si no puede hacerlo debido a un error de valor (ValueError), significa que estamos
tratando con una fecha en un año bisiesto (por ejemplo, 29 de febrero en un año bisiesto), por lo que agrega 4 años en
su lugar."""


def next_date(date_string):
  # Convert the argument from string to date object
  date_obj = datetime.datetime.strptime(date_string, r"%Y-%m-%d")
  next_date_obj = add_year(date_obj)

  # Convert the datetime object to string,
  # in the format of "yyyy-mm-dd"
  next_date_string = next_date_obj.strftime("%Y-%m-%d")
  return next_date_string


"""La función next_date toma una cadena date_string como entrada, que debe estar en el formato "year-month-day".
Convierte esta cadena en un objeto de fecha utilizando datetime.datetime.strptime.
Luego, llama a la función add_year para calcular la fecha del próximo año y almacena el resultado en next_date_obj.
Finalmente, convierte el objeto de fecha next_date_obj de nuevo en una cadena en el formato "year-month-day" utilizando strftime y lo devuelve como resultado."""


today = date.today()  # Get today's date
print(next_date(str(today)))
# Should return a year from today, unless today is Leap Day

print(next_date("2021-01-01")) # Should return 2022-01-01
print(next_date("2020-02-29")) # Should return 2024-02-29

"""El ejemplo al final del código muestra cómo usar la función next_date con diferentes entradas y lo que se espera como
salida. En resumen, esta función toma una fecha, calcula la fecha del próximo año (considerando los años bisiestos) y
devuelve la fecha resultante en el mismo formato."""
