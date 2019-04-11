def crear_funcion(operador):
  if operador == '+':
    def suma(val1,val2):
      return val1+val2
    return suma
  elif operador == '-':
    def resta(val1,val2):
      return val1-val2
    return resta
  elif operador == "*":
    def multiplicacion(val1,val2):
      return val1*val2
    return multiplicacion
  elif operador == "/":
    def division(val1,val2):
      return val1/val2
    return division
  else:
    return "Error"

def operacion(funcion, val1 = 0, val2 = 0):
	return funcion(val1,val2)