def multi_con_sumas(x,y):
	if x == 0:
		return 0
	else:
		return y + multi_con_sumas(x-1,y)

if __name__ == "__main__":
	print(multi_con_sumas(3,2))
