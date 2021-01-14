from com2_Leiva_Maira import es_bisiesto

def cant_dias_mes(mes,año):
    """Devuelve la cantidad de dias correspondientes al mes"""
    if mes in (1, 3, 5, 7, 8, 10, 12):
        return 31
    elif mes in (4, 6, 9, 11):
        return 30
    elif mes == 2 and es_bisiesto(año) == True:
        return 29
    else:
        return 28
