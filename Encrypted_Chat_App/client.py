import socket
import threading
from crypto_utils import encrypt, decrypt

client = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
client.connect(("127.0.0.1", 5555))

name = input("Enter your name: ")

# receive messages
def receive():
    while True:
        try:
            msg = client.recv(1024)
            print(decrypt(msg))
        except:
            print("Disconnected")
            break

# send messages
def write():
    while True:
        message = f"{name}: {input('')}"
        client.send(encrypt(message))

# threads for concurrency
threading.Thread(target=receive).start()
write()