import unittest
from src.models.electrodomestico import Electrodomestico 

class TestElectrodomestico(unittest.TestCase):
    def test_crear_electrodomestico(self):
        electrodomestico = Electrodomestico("001", "Televisor", "LG", 499.99)
        self.assertEqual(electrodomestico.codigo, "001")
        self.assertEqual(electrodomestico.nombre, "Televisor")
        self.assertEqual(electrodomestico.marca, "LG")
        self.assertEqual(electrodomestico.precio, 499.99)

if __name__ == "__main__":
    unittest.main()
