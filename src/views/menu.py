from src.controllers.almacen_controller import AlmacenController 

def mostrar_menu():
    almacen_controller = AlmacenController()
    
    while True:
        print("\nMenu del Almacen de Electrodomesticos")
        print("1. Agregar Electrodomestico")
        print("2. Listar Electrodomesticos")
        print("3. Buscar Electrodomestico")
        print("4. Eliminar Electrodomestico")
        print("5. Salir")
        
        opcion = input("Seleccione una opcion: ")

        if opcion == "1":
            codigo = input("Ingrese el codigo del electrodomestico: ")
            nombre = input("Ingrese el nombre del electrodomestico: ")
            marca = input("Ingrese la marca del electrodomestico: ")
            precio = float(input("Ingrese el precio del electrodomestico: "))
            almacen_controller.agregar_electrodomestico(codigo, nombre, marca, precio)
            print("Electrodomestico agregado con Exito")
        elif opcion == "2":
            electrodomesticos = almacen_controller.listar_electrodomesticos()
            for electrodomestico in electrodomesticos:
                print(electrodomestico)
        elif opcion == "3":
            codigo = input("Ingrese el codigo del electrodomestico a buscar: ")
            electrodomestico = almacen_controller.buscar_electrodomestico(codigo)
            if electrodomestico:
                print(electrodomestico)
            else:
                print("Electrodomestico no encontrado")
        elif opcion == "4":
            codigo = input("Ingrese el codigo del electrodomestico a eliminar: ")
            if almacen_controller.eliminar_electrodomestico(codigo):
                print("Electrodomestico eliminado con Exito")
            else:
                print("Electrodomestico no encontrado")
        elif opcion == "5":
            print("Saliendo...")
            break
        else:
            print("Opcion no válida")

