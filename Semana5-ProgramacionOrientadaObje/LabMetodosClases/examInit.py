class Elevator:
    def __init__(self, bottom, top, current):
        """Inicializa la instancia del Elevador."""
        self.bottom = bottom  # Piso mínimo al que puede ir el ascensor.
        self.top = top  # Piso máximo al que puede ir el ascensor.
        self.current = current  # Piso actual en el que se encuentra el ascensor.

    def up(self):
        """Hace que el ascensor suba un piso si no está en el piso más alto."""
        if self.current < self.top:
            self.current += 1

    def down(self):
        """Hace que el ascensor baje un piso si no está en el piso más bajo."""
        if self.current > self.bottom:
            self.current -= 1

    def go_to(self, floor):
        """Hace que el ascensor vaya al piso específico si está dentro del rango."""
        if self.bottom <= floor <= self.top:
            self.current = floor

    def __str__(self):
        """Devuelve una representación en cadena del estado actual del ascensor."""
        return "Current floor: {}".format(self.current)

# Crear una instancia de Elevator con límites de piso definidos
elevator = Elevator(-1, 10, 0)

# Prueba de ir al piso 5 y luego imprimir el ascensor
elevator.go_to(5)
print(elevator)  # Debería imprimir "Current floor: 5"
