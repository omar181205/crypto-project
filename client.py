import socket
from des import encrypt_ecb, pad, print_bits

HOST = "127.0.0.1"
PORT = 5000
KEY = b"BANK2026"

message = input("Enter your message: ")
while message.strip() == "":
    print("The message cannot be empty.")
    message = input("Enter your message: ")

data = message.encode("utf-8")
print()
print_bits("Message in binary (after padding):", pad(data))

encrypted = encrypt_ecb(data, KEY)
print()
print_bits("Encrypted in binary:", encrypted)
print()
print("Encrypted (hex):", encrypted.hex())

client = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
client.connect((HOST, PORT))
client.sendall(encrypted)
print("Sent to server.")
client.close()