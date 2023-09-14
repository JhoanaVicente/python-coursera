def network(servers):
    result = ""

    for hostname, IP_address in servers.items():
        result += "The IP address of the {} server is {}".format(hostname, IP_address) + "\n" # Salto de linea de texto("\n"
    return result

# Call the "network" function with the dictionary.
print(network({"Domain Name Server":"8.8.8.8", "Gateway Server":"192.168.1.1", "Print Server":"192.168.1.33", "Mail Server":"192.168.1.190"}))

# Should print:
# The IP address of the Domain Name Server server is 8.8.8.8
# The IP address of the Gateway Server server is 192.168.1.1
# The IP address of the Print Server server is 192.168.1.33
# The IP address of the Mail Server server is 192.168.1.190




def reset_scores(game_scores):
    new_game_scores = game_scores.copy()

    for player, score in new_game_scores.items():
        new_game_scores[player] = 0
    return new_game_scores

game1_scores = {"Arshi": 3, "Catalina": 7, "Diego": 6}

# Call the "reset_scores" function with the "game1_scores" dictionary.
print(reset_scores(game1_scores))
# Should print {'Arshi': 0, 'Catalina': 0, 'Diego': 0}

"""1. Se define la función `reset_scores` que acepta un diccionario llamado `game_scores`.

2. Se crea una copia del diccionario `game_scores` utilizando el método `copy()`. Esta copia se almacena en la variable
`new_game_scores`. La razón para crear una copia es que no queremos modificar el diccionario original `game_scores`, sino
crear un nuevo diccionario con puntajes restablecidos.

3. Se inicia un bucle `for` que recorre cada elemento del diccionario `new_game_scores`. Cada elemento del diccionario consiste
en un par clave-valor, donde la clave es el nombre del jugador y el valor es su puntaje actual.

4. Dentro del bucle, se establece el puntaje del jugador (`score`) en 0 para cada jugador en el diccionario `new_game_scores`.
Esto se hace asignando 0 al valor correspondiente en el diccionario usando `new_game_scores[player] = 0`.

5. Después de recorrer todos los jugadores en el diccionario, la función `reset_scores` devuelve el diccionario `new_game_scores`,
que ahora contiene los mismos jugadores, pero todos tienen un puntaje de 0.

6. Finalmente, se llama a la función `reset_scores` con el diccionario `game1_scores`, que contiene los puntajes originales
del juego. El resultado de la función se imprime usando `print()`.

La salida esperada cuando se llama a `reset_scores(game1_scores)` es un nuevo diccionario con los mismos jugadores, pero
todos los puntajes establecidos en 0"""
