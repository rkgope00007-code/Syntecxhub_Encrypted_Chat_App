from cryptography.hazmat.primitives.ciphers import Cipher, algorithms
from cryptography.hazmat.decrepit.ciphers import modes
import os

SECRET_KEY = b"thisisaverysecretkey123456789012"

def encrypt(message: str):
    iv = os.urandom(16)
    cipher = Cipher(algorithms.AES(SECRET_KEY), modes.CFB(iv))
    encryptor = cipher.encryptor()

    ciphertext = encryptor.update(message.encode()) + encryptor.finalize()
    return iv + ciphertext


def decrypt(data: bytes):
    iv = data[:16]
    ciphertext = data[16:]

    cipher = Cipher(algorithms.AES(SECRET_KEY), modes.CFB(iv))
    decryptor = cipher.decryptor()

    return (decryptor.update(ciphertext) + decryptor.finalize()).decode()