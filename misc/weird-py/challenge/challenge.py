#!/usr/bin/env python3

import ast

FLAG = "shellmates{Fl0At1N_p01nT5_nUM83r5_AR3_r3alY_w311111RD}"

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