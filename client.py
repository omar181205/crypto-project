import socket
from des import encrypt_ecb

HOST = "127.0.0.1"
PORT = 5000
KEY = b"BANK2026"

sender = input("Send from (client name/account): ")
receiver = input("Send to (client name/account): ")
amount = input("Amount: ")
while not amount.isdigit():
    print("Amount must be a number (digits only).")
    amount = input("Amount: ")

message = "TRANSFER $" + amount + " FROM " + sender + " TO " + receiver
print("Original message:", message)

encrypted = encrypt_ecb(message.encode(), KEY)
print("Encrypted (hex) :", encrypted.hex())

client = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
client.connect((HOST, PORT))
client.sendall(encrypted)
print("Sent to server.")
client.close()