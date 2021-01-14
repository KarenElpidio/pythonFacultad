def es_bisiesto(años):

    """Recibe por parámetro un número que representa un año,
    y devuelve un resultado booleano que indica si es, o no es, bisiesto."""
    
    if años % 400 == 0 and años % 4 == 0:
        return True
    elif años % 4 == 0 and años % 100 != 0:
        return True
    elif años % 100 == 0:
        return False
    else:
        return False

