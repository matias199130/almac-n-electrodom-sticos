class Electrodomestico:
    def __init__(self, codigo, nombre, marca, precio):
        self.codigo = codigo
        self.nombre = nombre
        self.marca = marca
        self.precio = precio

    def __str__(self):
        return f"Codigo: {self.codigo}, Nombre: {self.nombre}, Marca: {self.marca}, Precio: {self.precio}"
