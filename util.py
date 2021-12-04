import hashlib
import re
import AES, db

def get_sha256(string):
    return hashlib.sha256(string.encode())

def encrypt_and_store(username,to,amount):
    data=username+" "+to+" " +str(amount)
    tag,nonce,cyphertext=AES.encrypt(data.encode("utf8"))
    db.insert_transactions(tag,nonce,cyphertext)


def decrypt_and_update():
    record=db.get_latest_transaction()
    plaintext=AES.decrypt(record['tag'],record['encrypted_data'],record['nonce'])
    arr=plaintext.split()
    db.remove_amount(arr[0],int(arr[2]))
    db.add_amount(arr[1],int(arr[2]))

