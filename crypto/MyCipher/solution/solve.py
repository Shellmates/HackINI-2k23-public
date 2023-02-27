from pwn import xor
from Crypto.Util.number import bytes_to_long,long_to_bytes, getPrime

def decrypt_to_flag(enc):
    return xor(enc,b"leet")

def decrypt_to_stage1(enc):
    e = 65537
    p = 61571454303089397514579603620349373049341652571832994202527081254304368292533
    q = 59664824358038218622178548968528898444289564045465867369823072940589283303949
    n = p*q
    phi = (p-1)*(q-1)
    d = pow(e,-1,phi)
    return long_to_bytes(pow(bytes_to_long(enc),d,n))

def decrypt_to_stage2(enc3):
    res = b''
    start = 0
    if len(enc3)%2 == 0:    
        end = len(enc3)-1
    else:
        end = len(enc3)

    for i in range(start,end,2):
        res += long_to_bytes(enc3[i])

    end = 0
    if len(enc3)%2 == 0:
        start = len(enc3)-1
    else:
        start = len(enc3)-2

    for i in range(start,end,-2):
        res += long_to_bytes(enc3[i])
    
    return res

def decrypt(enc):
    return decrypt_to_flag(decrypt_to_stage1(decrypt_to_stage2(enc)))

enc = open("enc.bin","rb").read()
print(decrypt(enc))