import re
import unittest

my_txt = "An investment in knowledge pays the best interest."

def LetterCompiler(txt):
    result = re.findall(r'([a-c]).', txt)
    return result
print(LetterCompiler(my_txt))

"""LetterCompiler(txt):
Esta función toma un argumento de texto (txt).
Utiliza la función re.findall para buscar todas las letras 'a', 'b' o 'c' seguidas de cualquier otro carácter en el texto.
Devuelve una lista de las letras encontradas."""



class TestCompiler(unittest.TestCase):
    def test_basic(self):
        testcase = "The best preparation for tomorrow is doing your best today."
        expected = ['b', 'a', 'a', 'b', 'a']
        self.assertEqual(LetterCompiler(testcase), expected)

unittest.main(argv = ['first-arg-is-ignored'], exit = False)

"""TestCompiler:
Esta clase de pruebas hereda de unittest.TestCase.
Contiene el método de prueba test_basic, que prueba la función LetterCompiler con una cadena de entrada específica.
Compara el resultado de la función con un valor esperado utilizando self.assertEqual para asegurarse de que el resultado sea correcto.
Ejecuta las pruebas con unittest.main() al final de la clase."""



class TestCompiler2(unittest.TestCase):
    def test_two(self):
        testcase = "A b c d e f g h i j k l m n o q r s t u v w x y z"
        expected = ['b', 'c']
        self.assertEqual(LetterCompiler(testcase), expected)

# EDGE CASES HERE
unittest.main(argv = ['first-arg-is-ignored'], exit = False)

"""TestCompiler2:
Esta es otra clase de pruebas que también hereda de unittest.TestCase.
Contiene el método de prueba test_two, que prueba la función LetterCompiler con una cadena de entrada diferente.
Compara el resultado con un valor esperado usando self.assertEqual.
Al igual que TestCompiler, ejecuta las pruebas con unittest.main() al final de la clase."""


"""Al final del script, tienes dos llamadas a unittest.main(). La primera ejecuta las pruebas de la clase TestCompiler, y 
la segunda ejecuta las pruebas de la clase TestCompiler2. Si ambos conjuntos de pruebas se ejecutan sin errores y obtienen
resultados "OK", eso significa que las pruebas han pasado con éxito y que la función LetterCompiler funciona según lo
esperado para los casos de prueba proporcionados."""
