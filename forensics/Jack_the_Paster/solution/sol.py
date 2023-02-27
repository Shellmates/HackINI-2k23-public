from pwn import xor

xored = open("flag.png.enc","rb").read()
normal = open("solution/standard.png","rb").read()

key = xor(xored[:16], normal[:16])

recovered = xor(xored, key)
open("flag.png","wb").write(recovered)

