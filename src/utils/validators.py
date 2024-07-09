def validar_codigo(codigo):
    # Verifica que el código no esté vacío y sea una cadena
    if not codigo or not isinstance(codigo, str):
        return False
    return True

def validar_precio(precio):
    # Verifica que el precio sea un número positivo
    try:
        precio = float(precio)
        if precio < 0:
            return False
    except ValueError:
        return False
    return True
