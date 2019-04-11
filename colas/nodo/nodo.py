
def agregarNodo(cola,max,valor):
    if len(cola) == max :
        return print("La cola esta llena")
    else:
        cola.append(valor)
        print("Nodo agregado")
        return cola
            
def eliminarNodo(cola):
    auxiliar = cola[len(cola)-1]
    nueva_cola = [numero for numero in cola if numero != auxiliar]
    return nueva_cola

def buscarValor(cola,actual, valor, size):
    if valor == cola[actual]:
        print("valor encontrado en la posicion "+str(actual))
        return actual
    elif size >= len(cola)-1:
        print("Error no se encontro el dato")
        return False
    else:
        return buscarValor(cola, actual+1 , valor , size)