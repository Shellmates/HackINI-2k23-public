from pwn import xor
from SECRET import flag
from Crypto.Util.number import bytes_to_long,long_to_bytes, getPrime

def phase1(string):
    return xor(b'leet', string)

def phase2(var):
    e = 65537
    p = 61571454303089397514579603620349373049341652571832994202527081254304368292533
    q = 59664824358038218622178548968528898444289564045465867369823072940589283303949
    n = p*q
    return long_to_bytes(pow(bytes_to_long(var),e,n))

def phase3(val):
    res=b''
    for i in range(int(len(val)/2)):
        res += long_to_bytes(val[i])
        res += long_to_bytes(val[len(val)-i-1])
    
    if (len(val)%2!=0):
        res += long_to_bytes(val[int(len(val)/2)])
    
    return res


enc1 = phase1(flag)
enc2 = phase2(enc1)
enc3 = phase3(enc2)

open("enc.bin","wb").write(enc3)