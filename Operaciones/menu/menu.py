import operaciones.operaciones as operaciones
def menu():
    bandera = True
    while(bandera):
        print("*"*20)
        print("Bienvenido a las operaciones ITM")
        print("Escriba 1 para sumar dos valores")
        print("Escriba 2 para restar dos valores")
        print("Escriba 3 para multiplicar dos valores")
        print("Escriba 4 para dividir dos valores")
        print("Escriba 5 para salir")
        selec = seleccion(int(input("Escribe su seleccion: ")))
        if selec == False:
            bandera = False
        else:
            operacion = operaciones.crear_funcion(selec)
            print( "Resultado es "+ str(operaciones.operacion(operacion, 
            int(input("Escriba valor 1: ")),
            int(input("Escriba valor 2: "))
            )))
            
def seleccion(num_e):
    if num_e == 1:
        return '+'
    elif num_e == 2:
        return '-'
    elif num_e == 3:
        return '*'
    elif num_e == 4:
        return '/'
    elif num_e == 5:
        return False