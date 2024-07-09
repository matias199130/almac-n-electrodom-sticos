from src.models.electrodomestico import Electrodomestico

class AlmacenController:
    def __init__(self):
        self.electrodomesticos = []

    def agregar_electrodomestico(self, codigo, nombre, marca, precio):
        nuevo_electrodomestico = Electrodomestico(codigo, nombre, marca, precio)
        self.electrodomesticos.append(nuevo_electrodomestico)
        return nuevo_electrodomestico

    def listar_electrodomesticos(self):
        return self.electrodomesticos

    def buscar_electrodomestico(self, codigo):
        for electrodomestico in self.electrodomesticos:
            if electrodomestico.codigo == codigo:
                return electrodomestico
        return None

    def eliminar_electrodomestico(self, codigo):
        for i, electrodomestico in enumerate(self.electrodomesticos):
            if electrodomestico.codigo == codigo:
                del self.electrodomesticos[i]
                return True
        return False
