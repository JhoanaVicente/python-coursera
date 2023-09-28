import unittest
from validations import validate_user
"""Importas el módulo unittest para usar sus funciones y clases de prueba.
Importas la función validate_user desde el módulo validations. Esta función es la que deseas probar."""

class TestValidateUser(unittest.TestCase):
# CLASE DE PRUEBA: Defines una clase llamada TestValidateUser que hereda de unittest.TestCase. Esta clase contendrá tus pruebas unitarias.

#PRUEBAS UNITARIAS:
    def test_valid(self):
        self.assertEqual(validate_user("validuser", 3), True)
    """Define una prueba llamada test_valid. En esta prueba, se llama a validate_user con el argumento "validuser"
    y una longitud mínima de 3. Luego, se utiliza self.assertEqual para verificar si el resultado de validate_user es igual a True."""


    def test_too_short(self):
        self.assertEqual(validate_user("inv", 5), False)
    """Define otra prueba llamada test_too_short. En esta prueba, se llama a validate_user con el argumento "inv" y una
    longitud mínima de 5. Luego, se utiliza self.assertEqual para verificar si el resultado de validate_user es igual a False."""


    def test_invalid_characters(self):
        self.assertEqual(validate_user("invalid_user", 1), False)
    """Define una prueba llamada test_invalid_characters. En esta prueba, se llama a validate_user con el argumento "invalid_user"
    y una longitud mínima de 1. Luego, se utiliza self.assertEqual para verificar si el resultado de validate_user es igual a False."""


    def test_invalid_minlen(self):
        with self.assertRaises(ValueError):
            validate_user("user", -1)
    """Define otra prueba llamada test_invalid_minlen. En esta prueba, se utiliza el contexto with self.assertRaises(ValueError)
    para verificar que cuando se llama a validate_user con un valor negativo para la longitud mínima, se debe generar una excepción ValueError."""


if __name__ == '__main__':
    unittest.main()
"""Esta parte del código verifica si el script se está ejecutando directamente (no se está importando como un módulo). Si se
ejecuta directamente, se inicia la ejecución de las pruebas unitarias utilizando unittest.main()."""



"""En resumen, este código define un conjunto de pruebas unitarias para la función validate_user, donde cada prueba verifica
un aspecto específico del comportamiento de la función. Cuando ejecutes este script, unittest ejecutará todas las pruebas
y te mostrará los resultados para verificar si la función validate_user funciona correctamente en diferentes situaciones."""
