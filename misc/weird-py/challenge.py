import ast

FLAG = "shellmates{XXXXXXXXXXXXXXXXXXXXXXXXXX}"

if __name__ == '__main__':
	try:
		a = ast.literal_eval(input("Enter a: "))
		assert isinstance(a, (int,float)), True
		b = ast.literal_eval(input("Enter b: "))
		assert isinstance(b, (int,float)), True
	except:
		print("Only numbers are allowed")
		exit()

	if (a/b).is_integer() and (a%b != 0):
		print(FLAG)
	else:
		print("Try again!")
