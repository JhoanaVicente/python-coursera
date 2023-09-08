# MÉTODO STR DEVUELVE LA CADENA QUE QUEREMOS IMPRIMIR

class Apple:
    def __init__(self, color, flavor):
        self.color = color
        self.flavor = flavor
    def __str__(self):
        return "this apple is {} and its flavor is {}".format(self.color, self.flavor)
jonagold = Apple("red", "sweet")
print(jonagold)

help(Apple) #DOCSTRINGS (PARA SABER QUE FUNCION HAS USADO
"""Las cadenas de documentos son muy útiles para documentar nuestras clases, métodos y funciones personalizadas, pero
también cuando trabajamos con nuevas bibliotecas o funciones. ¡Estarás extremadamente agradecido por las cadenas de
documentación cuando tengas que trabajar con código que otra persona escribió!"""
