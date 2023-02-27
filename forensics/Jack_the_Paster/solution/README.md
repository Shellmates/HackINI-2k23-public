# Jack the Paster

## Write-up

Deobfuscate the code, then use any png to unxor the flag.
```python
from pwn import xor

xored = open("flag.png.enc","rb").read()
normal = open("standard.png","rb").read()

key = xor(xored[:16], normal[:16])

recovered = xor(xored, key)
open("flag.png","wb").write(recovered)
```
## Flag

`shellmates{I_r3ally_wanteD_t0_play_codcodcod}`
