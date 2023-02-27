from base64 import b64encode,b32encode,b16encode



FLAG = b'shellmates{b4$3$_16_32_64}'
res = b64encode(b32encode(b16encode(FLAG)))

with open('file.txt' , 'wb+') as f :
    f.write(res)
