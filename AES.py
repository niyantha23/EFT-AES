from Crypto.Cipher import AES
from Crypto import Random 
import random

def encrypt(data):
    key = b'Sixteen byte key'
    aes = AES.new(key, AES.MODE_EAX)
    nonce=aes.nonce
    encrypted,tag = aes.encrypt_and_digest(data)
    return tag, nonce,encrypted
data="niyantha is my name"
a,b,c=encrypt(data.encode("utf8"))    
#print(a)
#print(b)
#print(c)


def decrypt(tag,encrypted, nonce):
    key = b'Sixteen byte key'
    cipher = AES.new(key, AES.MODE_EAX, nonce=nonce)
    plaintext = cipher.decrypt(encrypted)
    try:
        cipher.verify(tag)
        return print( plaintext.decode())
    except ValueError:
        return print("Key incorrect or message corrupted")

decrypt(a,c,b)

