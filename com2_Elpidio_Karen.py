from com2_Leiva_Maira import es_bisiesto

def fecha_siguiente(año, mes, dia):
    """ El usuario ingresa una fecha en números (día, mes, año), 
    y esta devuelva como resultado la fecha (día, mes, año) del día sigunte """

    if mes in (1, 3, 5, 7, 8, 10, 12):
        dias_mes = 31
    elif mes == 2:
        if es_bisiesto(año) == True:
            dias_mes = 29
        else:
            dias_mes = 28
    else:
        dias_mes = 30

    if dia < dias_mes:
        dia += 1
    else:
        dia = 1
        if mes == 12:
            mes = 1
            año += 1
        else:
            mes += 1
    
    return (año, mes, dia)
