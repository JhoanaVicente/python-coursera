def is_power_of(number, base):
  # Base case: when number is smaller than base.
  if number < base:
    # If number is equal to 1, it's a power (base**0).
    return number == 1

  # Recursive case: keep dividing number by base.
  return is_power_of(number // base, base)

print(is_power_of(8,2)) # Should be True
print(is_power_of(64,4)) # Should be True
print(is_power_of(70,10)) # Should be False

"""El caso base verifica si number es menor que base. Si es así, la función verifica si number es igual a 1. 
Si es igual a 1, significa que number es una potencia de base**0, por lo que retorna True. 
De lo contrario, retorna False. El caso recursivo se activa si number es mayor o igual que base. En este caso,
la función se llama a sí misma con el argumento number // base, lo que efectivamente reduce number dividiéndolo por base. 
Continúa llamando a la función de manera recursiva hasta que se alcance el caso base.
Cuando el número llega al caso base (cuando es menor que la base), se verifica si el número es igual a 1. 
Si es igual a 1, es una potencia de base**0, y se devuelve True. Si no es igual a 1, se devuelve False."""""
