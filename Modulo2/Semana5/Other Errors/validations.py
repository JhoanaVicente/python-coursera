def validate_user(username, minlen):
    # Verificar si el primer argumento (username) es una cadena (str)
    assert type(username) == str, "username must be a string"

    # Verificar si minlen es un valor válido
    if minlen < 1:
        raise ValueError("minlen must be at least 1")

    # Verificar si la longitud del nombre de usuario es menor que minlen
    if len(username) < minlen:
        return False

    # Verificar si el nombre de usuario contiene solo caracteres alfanuméricos
    if not username.isalnum():
        return False

    # Si todas las verificaciones anteriores pasan, entonces el nombre de usuario es válido
    return True


# COMENTO ESTO PARA QUE ME FUNCIONE EL TESTINGERRORS.PY
print(validate_user("", 1))
print(validate_user("myuser", 1))
print(validate_user(88, 1))
print(validate_user([], 1))
print(validate_user(["name"], 1))
print(validate_user([3], 1))
