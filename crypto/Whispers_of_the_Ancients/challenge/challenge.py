#!/usr/bin/env python3

from config import FLAG,key


def encrypt(plaintext, key):
    key= key.lower()
    ciphertext = ""
    key_i=0
    for i in range(len(plaintext)):
        char = plaintext[i]
        if char.isalpha():
            if char.islower():
                low=True
            else:
                low=False
                char = char.lower()
            enc_char = chr((((ord(char)-97) + (ord(key[key_i%len(key)])-97)) % 26)+97)
            if not low:
                enc_char = enc_char.upper()
            key_i+=1
        else:
            enc_char = char
        ciphertext += enc_char

    return ciphertext 

def decrypt():
    print("Nah Nah Nah")


def main():
   
    
    print('Welcome H4cK3r')
    while True:
        print('now choose your side:\n\t1) encrypt data\n\t2) decrypt data\n\t3) get the flag\n\t4) exit')
        choice = input('>> ')
        if choice == "1": 
            print('What do you want to encrypt?')
            pt = input('> ')
            print(encrypt(pt,key))
            
        elif choice == "2":
             decrypt()
            
        elif choice == "3":
            print(f"Did you really tought I would easily give you the flag, but since you asked for it here is the encrypted flag: ")
            print(f'The encrypted flag is: {encrypt(FLAG,key)}')
        
        elif choice == "4":
             exit()
            
        else:
            print("you have to choose between 1,2,3 or 4")
        
if __name__ == "__main__":
        main()