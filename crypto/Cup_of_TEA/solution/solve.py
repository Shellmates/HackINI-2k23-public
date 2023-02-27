from Crypto.Util.number import long_to_bytes,bytes_to_long
from config import ct,key


K = [bytes_to_long(key[i:i+4])  for i in range(0,len(key),4)]

def decrypt(ciphertext):
    plaintext = b""
    
    for L,R in ciphertext:

        delta = 0x9e3779b9
        sum = delta << 5
        
        for i in range(32):
            R -= ((L << 4) + K[2]) ^ (L + sum) ^ ((L >> 5) + K[3])
            L -= ((R << 4) + K[0]) ^ (R + sum) ^ ((R >> 5) + K[1])
            sum -= delta

            
        L = long_to_bytes(L)
        R = long_to_bytes(R)
        block = L+R
        plaintext += block

    return plaintext

if __name__ == "__main__":
    print(decrypt(ct))
