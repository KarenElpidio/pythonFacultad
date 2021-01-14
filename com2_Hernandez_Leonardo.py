from com2_Lopez_Leonardo import fecha_valida
from com2_Elpidio_Karen import fecha_siguiente

def main():
    """Funcion principal del programa, se encarga de validar los datos y devolver el dia siguiente."""

    print('Todos los valores introducidos deben ser numericos\n')
    
    año = int(input("Introduzca un año: "))
    mes = int(input("Introduzca un mes: "))
    dia = int(input("Introduzca un dia: "))

    while fecha_valida(dia, mes, año) == False:

        print("\nFecha no valida, vuelva a ingresarla")

        año = int(input("Introduzca un año: "))
        mes = int(input("Introduzca un mes: "))
        dia = int(input("Introduzca un dia: "))

    año2, mes2, dia2 = fecha_siguiente(año,mes,dia)

    print("""
        La fecha que ingreso fue \n
        El año {} del mes {} del dia {} \n
        La fecha siguiente es: \n
        El año {} del mes {} del dia {}
        """.format(año, mes, dia, año2, mes2, dia2))

    pausa = input("Presione enter para salir...")

main()

