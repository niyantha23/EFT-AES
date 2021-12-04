import hashlib
import AES, db

def get_sha256(string):
    return hashlib.sha256(string.encode())

def encrypt_and_store(username,to,amount):
    data=username+to+str(amount)
    tag,nonce,cyphertext=AES.encrypt(data.encode("utf8"))
    db.insert_transactions(tag,nonce,cyphertext)


