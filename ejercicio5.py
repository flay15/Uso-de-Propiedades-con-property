class Producto:
    def __init__(self, nombre, precio):
        self._nombre = nombre
        self._precio = precio

    @property
    def nombre(self):
        return self._nombre

    @property
    def precio(self):
        return self._precio

    @precio.setter
    def precio(self, nuevo_precio):
        if nuevo_precio >= 0:
            self._precio = nuevo_precio
        else:
            print("Error: El precio no puede ser negativo.")

    def mostrar_informacion(self):
        print(f"Producto: {self.nombre}, Precio: ${self.precio}")

producto = Producto("Laptop", 1500)
producto.mostrar_informacion()

producto.precio = 1200  # Cambiar el precio
producto.mostrar_informacion()

producto.precio = -500  # Intento de precio negativo
