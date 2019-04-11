def fibonacci(size,anterior,actual):
	if size == 1:
		return anterior
	else:
		print(anterior)
		return fibonacci(size - 1, actual, anterior + actual )

if __name__ == "__main__":
	print(fibonacci(5,0,1))