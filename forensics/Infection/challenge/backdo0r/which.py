#!/usr/bin/python3
import sys

if sys.argv[1]=='ls':
	print("ls: aliased to ls --color=tty")
else:
	print("/usr/bin/" + sys.argv[1])