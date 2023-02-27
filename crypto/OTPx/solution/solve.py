from pwn import xor

ciphertext= b'a\xf2\xbd\r\xe2\x96m\xea\xfesi\xf5\x96$\xa3\xafE\xf3\xfe_B\xdb\x9c>\xe1\xaf|\xc1\xe3o`\xe7'
Hint=b'shellmates'
def decrypt_OTP(ciphertext,Hint):   
    l_hint=len(Hint)
    for i in range(0,len(ciphertext)):
        key=xor(Hint,ciphertext[i:i+l_hint])
        plaintext=xor(ciphertext ,key)
        if Hint in plaintext :
            return plaintext

print(decrypt_OTP(ciphertext, Hint))