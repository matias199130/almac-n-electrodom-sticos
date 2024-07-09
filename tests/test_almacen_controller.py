import unittest
from src.controllers.almacén_controller import AlmacenController # type: ignore

class TestAlmacenController(unittest.TestCase):
    def setUp(self):
        self.controller = AlmacenController()

    def test_agregar_electrodomestico(self):
        self.controller.agregar_electrodomestico("001", "Televisor", "LG", 499.99)
        self.assertEqual(len(self.controller.electrodomesticos), 1)

    def test_buscar_electrodomestico(self):
        self.controller.agregar_electrodomestico("001", "Televisor", "LG", 499.99)
        electrodomestico = self.controller.buscar_electrodomestico("001")
        self.assertIsNotNone(electrodomestico)

    def test_eliminar_electrodomestico(self):
        self.controller.agregar_electrodomestico("001", "Televisor", "LG", 499.99)
        result = self.controller.eliminar_electrodomestico("001")
        self.assertTrue(result)
        self.assertEqual(len(self.controller.electrodomesticos), 0)

if __name__ == "__main__":
    unittest.main()
