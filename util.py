import hashlib

def get_sha256(string):
    return hashlib.sha256(string.encode())
