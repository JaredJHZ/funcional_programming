def getCola(max,cola):
    return (max,cola)

def iniciarCola(max,funcion = getCola):
    cola = []
    return funcion(max,cola)

def recorrerCola(cola,size,forma = ""):
    if size == 0 :
        forma += str(cola[size])
        print(forma)
        return False
    else:
        forma += str(cola[size]) + "-"
        return recorrerCola(cola,size - 1, forma)

def ordenar(cola):
    return bubbleSortMejorado(cola,0,len(cola)-1)

def bubbleSortMejorado(cola,pointer1,pointer2):
    if pointer1 >= len(cola):
        return cola
    else:
        if pointer2 <= pointer1:
            
            return bubbleSortMejorado(cola, pointer1+1  , len(cola)-1 )
    
        nuevaCola = intercambio(cola,pointer2)

        if nuevaCola:
            return bubbleSortMejorado(nuevaCola,pointer1,pointer2-1)
        else:
            return bubbleSortMejorado(cola,pointer1,pointer2-1)


def intercambio(cola, indice):
    nuevaCola = []
    if cola[indice-1] > cola[indice]:
        auxiliar = cola[indice]
        cola[indice] = cola[indice-1]
        cola[indice-1] = auxiliar
        nuevaCola = cola
        return nuevaCola
    else:
        return False

def printFinal(cola):
    print(cola[len(cola-1)])

def printPrincipio(cola):
    print(cola[0])