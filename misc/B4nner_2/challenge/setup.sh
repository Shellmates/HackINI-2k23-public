#!/bin/sh

mkdir /opt/pylib

echo "import sys
sys.path.append(\"/opt/pylib\")
" >> /etc/python3.10/sitecustomize.py

umask 113

echo "import hashlib

def filehash(file):
        HashMethod = hashlib.sha256()
        HashMethod.update(file.read())
        return(HashMethod.hexdigest() + ' - ' + file.name)
" > /opt/pylib/flaglib.py

chown root:ctf-cracked /opt/pylib/flaglib.py
