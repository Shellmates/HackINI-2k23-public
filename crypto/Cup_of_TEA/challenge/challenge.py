from Crypto.Util.number import bytes_to_long
import os

key = os.urandom(16)
K = [bytes_to_long(key[i:i+4]) for i in range(0,len(key),4)]

def encrypt(plaintext):
    ciphertext = []
    plaintext += "0" * (8 - len(plaintext) % 8)

    for i in range(0,len(plaintext),8):
        block = plaintext[i:i+8]
        L = block[0:4]
        R = block[4:8]
        
        L = bytes_to_long(L.encode())
        R = bytes_to_long(R.encode())

        delta = 0x9e3779b9
        sum = 0
        for i in range(32):
            sum += delta
            L += ((R << 4) + K[0]) ^ (R + sum) ^ ((R >> 5) + K[1])
            R += ((L << 4) + K[2]) ^ (L + sum) ^ ((L >> 5) + K[3])
        block = (L , R)

        ciphertext.append(block)


    return ciphertext


if __name__ == "__main__":
    plaintext = "FLAG"
    ciphertext = encrypt(plaintext)
    with open("config.py", "w") as w:
        w.write(f"key = {key}\n")
        w.write(f"ct = {str(ciphertext)}")
    
