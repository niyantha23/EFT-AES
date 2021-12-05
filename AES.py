from Crypto.Cipher import AES
from Crypto.Random import get_random_bytes

key = get_random_bytes(16)

def encrypt(data):
    # key = b'Sixteen byte key'
    aes = AES.new(key, AES.MODE_EAX)
    nonce=aes.nonce
    encrypted,tag = aes.encrypt_and_digest(data)
    return tag, nonce,encrypted

# data="The man in the high castle"
# a,b,c=encrypt(data.encode("utf8"))    
# print(a)
# print(b)
# print(c)


def decrypt(tag,encrypted, nonce, key1):
    # key = b'Sixteen byte key'
    cipher = AES.new(key1, AES.MODE_EAX, nonce=nonce)
    plaintext = cipher.decrypt(encrypted)
    try:
        cipher.verify(tag)
        return plaintext.decode()
    except ValueError:
        return print("Key incorrect or message corrupted")

# print(decrypt(a,c,b))