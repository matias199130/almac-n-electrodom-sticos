# Especificación Técnica del Proyecto de Almacén de Electrodomésticos

## Descripción General

Este documento describe los detalles técnicos del proyecto de consola en Python para gestionar un almacén de electrodomésticos. La aplicación permite agregar, listar, buscar y eliminar productos del almacén.

## Requisitos Funcionales

1. **Agregar Datos**: El sistema debe permitir al usuario ingresar nuevos electrodomésticos al almacén, incluyendo un código, nombre, marca y precio.
2. **Listar Datos**: El sistema debe listar todos los electrodomésticos en el almacén, mostrando toda su información relevante.
3. **Buscar Datos**: El sistema debe permitir al usuario buscar electrodomésticos por su código.
4. **Eliminar Datos**: El sistema debe permitir al usuario eliminar electrodomésticos del almacén por su código.
5. **Menú de Opciones**: El sistema debe presentar un menú con opciones para las funcionalidades mencionadas.

## Requisitos No Funcionales

1. **Interfaz de Usuario**: La interfaz debe ser de consola, fácil de usar e interactiva.
2. **Validación de Datos**: El sistema debe validar la entrada del usuario para minimizar errores, como asegurar que el precio sea un número positivo.

## Arquitectura del Sistema

El sistema se divide en varias capas para mantener la separación de responsabilidades:

1. **Modelos**: Define las clases que representan los datos.
2. **Controladores**: Contiene la lógica de negocio y la manipulación de datos.
3. **Vistas**: Maneja la interfaz de usuario y la interacción con el usuario.
4. **Utilidades**: Funciones auxiliares como validaciones.

## Detalles de Implementación

- **Lenguaje de Programación**: Python 3.x
- **Bibliotecas Utilizadas**: Ninguna biblioteca externa es requerida.

## Estructura del Proyecto

```
almacen-electrodomesticos/
├── README.md
├── .gitignore
├── main.py
├── src/
│ ├── models/
│ │ └── electrodomestico.py
│ ├── controllers/
│ │ └── almacén_controller.py
│ ├── views/
│ │ └── menu.py
│ └── utils/
│ └── validators.py
├── tests/
│ ├── test_electrodomestico.py
│ └── test_almacén_controller.py
└── docs/
└── especificacion_tecnica.md
```