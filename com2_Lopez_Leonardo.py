from com2_Nowicki_Martina import cant_dias_mes

def fecha_valida(dia,mes,anio):                                           
    """Chequea el dia, mes y año introducidos para verificar si es un dia valido"""
    
    #comprobacion de meses validos
    if(mes < 1 or mes > 12):
        return False
        
    #comprobacion de dias validos
    if (dia <= 0 or dia > cant_dias_mes(mes,anio)):
        return False

    #anio
    if(anio < 1):
        return False 

    #si los datos son correctos da un True
    return True
    


    