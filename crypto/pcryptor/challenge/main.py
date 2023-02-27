from Crypto.Cipher import AES
import base64
import random

MIN_RANGE = 1
MAX_RANGE = 10000000000
ENCRYPT_MSSG = "Message to encrypt : "
OUT_FILENAME = "enc"
DEFAULT_SEED = 10
KEY_LEN = 16

genKey = lambda : bytes([random.randint(0, 255) for _ in range(KEY_LEN)])

class Encryptor:
    def __init__(self, seed = DEFAULT_SEED):
        self.__seed = seed
    
    def setSeed(self):
        random.seed(self.__seed)

    def pad(self, plaintext):
        padding = b' ' * (16 - len(plaintext) % 16)
        return plaintext + padding

    def encrypt(self, mssg):
        plaintext = mssg.encode()
        plaintext = self.pad(plaintext)
        key = genKey()
        cipher = AES.new(key, AES.MODE_ECB)

        ciphertext = cipher.encrypt(plaintext)

        return base64.b64encode(ciphertext).decode()

# creating a new instance of the encryptor
encryptor = Encryptor()

# setting the __seed to a random unpredictable value
encryptor.__seed = random.randint(MIN_RANGE, MAX_RANGE)

# updating the random seed value
encryptor.setSeed()

# readin user input 
mssg = input(ENCRYPT_MSSG)

# encrypting the uesr input
enc = encryptor.encrypt(mssg)

with open(OUT_FILENAME, "w") as f:
    f.write(enc)

