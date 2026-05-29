import socket
import threading
import datetime
from crypto_utils import decrypt

HOST = "127.0.0.1"
PORT = 5555

server = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
server.bind((HOST, PORT))
server.listen()

clients = []

print("[STARTED] Server is running...")

# broadcast message to all clients
def broadcast(message, sender):
    for client in clients:
        if client != sender:
            client.send(message)

# handle each client
def handle_client(client):
    while True:
        try:
            encrypted_msg = client.recv(1024)

            # decrypt for logging only
            message = decrypt(encrypted_msg)
            print("[MSG]", message)

            # log messages
            time = datetime.datetime.now().strftime("%Y-%m-%d %H:%M:%S")
            with open("chat_log.txt", "a") as f:
                f.write(f"{time} - {message}\n")

            # re-send encrypted to others
            broadcast(encrypted_msg, client)

        except:
            clients.remove(client)
            client.close()
            break

# accept multiple clients (CONCURRENCY)
def receive():
    while True:
        client, addr = server.accept()
        print("[CONNECTED]", addr)

        clients.append(client)

        thread = threading.Thread(target=handle_client, args=(client,))
        thread.start()

receive()