import cola.cola as cola
import nodo.nodo as nodo

activado = True
def menu(queue = [], tupla = (), activado = True, primera = True):
    if activado == False:
        return False
    else:
        if primera:
            tupla = cola.iniciarCola(5)
            ejerCol = tupla[1]
            return menu(ejerCol,tupla,True,False)
        else:
            ejerCol = queue
            print("Bienvenido al menu de colas de ITM")
            print("*"*5)
            print("1 para agregar")
            print("2 para eliminar")
            print("3 para ordenar")
            print("4 para buscar")
            print("5 para imprimir")
            print("6 para imprimir el final de la cola")
            print("7 para imprimir el inicio de la cola")
            print("8 para salir")
            eleccion = seleccionar(int(input("Ingrese la opcion: ")))
            if eleccion == 1:
                ejerCol = nodo.agregarNodo(ejerCol,tupla[0],int(input("Agregar un valor: ")))
                return menu(ejerCol,tupla,True,False)
            elif eleccion == 2:
                ejerCol = nodo.eliminarNodo(ejerCol)
                return menu(ejerCol,tupla,True,False)
            elif eleccion == 3:
                ejerCol = cola.ordenar(ejerCol)
                return menu(ejerCol,tupla,True,False)
            elif eleccion == 4:
                nodo.buscarValor(ejerCol,0,int(input("Seleccione el valor a buscar: ")), len(ejerCol)-1)
                return menu(ejerCol,tupla,True,False)
            elif eleccion == 5:
                cola.recorrerCola(ejerCol,len(ejerCol)-1)
                return menu(ejerCol,tupla,True,False)
            elif eleccion == 6:
                cola.printFinal(ejerCol)
                return menu(ejerCol,tupla,True,False)
            elif eleccion == 7:
                cola.printPrincipio(ejerCol)
                return menu(ejerCol,tupla,True,False)
            elif eleccion == 8:
                activado = False
                return menu(ejerCol,tupla,False,False)
    






def seleccionar(num):
    if num > 8 :
        return print("Error ,ingrese la opcion otra vez")
    else:
        return num