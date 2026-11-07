import socket
from des import decrypt_ecb, print_bits

HOST = "127.0.0.1"
PORT = 5000
KEY = b"BANK2026"

server = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
server.setsockopt(socket.SOL_SOCKET, socket.SO_REUSEADDR, 1)
server.bind((HOST, PORT))
server.listen(1)
print("Server waiting for the client...")

conn, address = server.accept()
print("Client connected:", address)

data = b""
while True:
    chunk = conn.recv(4096)
    if not chunk:
        break
    data = data + chunk

print()
print_bits("Received in binary:", data)
print()
print("Received (hex):", data.hex())

try:
    message = decrypt_ecb(data, KEY)
    print()
    print_bits("Decrypted in binary:", message)
    print()
    print("Decrypted message:", message.decode("utf-8"))
except ValueError as error:
    print("Could not decrypt:", error)

conn.close()
server.close()