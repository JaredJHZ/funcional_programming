#Funcion recursiva 
def funcionRecursiva(c, n , lista):
	if n == 0 or c == "a": #estado base 1
		return lista
	else: #en caso de que no se cumpla el estado base
		c = input("Escriba una letra: ")[0] #Se toma solo la primera letra
		if c.isalpha(): # la variable c tiene que ser una letra
			lista.append(c) # Se agrega el valor a la lista
			return funcionRecursiva(c, n-1, lista)
		else:
			print("Tiene que escribir una letra: ")
			return funcionRecursiva(c, n, lista)

		
if __name__ == "__main__":
	n = "inicio" #Constante inicio para dar arranque al programa
	while type(n) != int:
		try:
			n = int(input("Escriba el numero de letras que desea agregar: "))
			lista = funcionRecursiva(None,n,[])
			print(lista)
		except:
			print("Tiene que seleccionar numero")