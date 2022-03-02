from http import client
import socket

target_host = '192.168.1.26'
target_port = 9998

client = socket.socket(socket.AF_INET, socket.SOCK_STREAM)

client.connect((target_host, target_port))

client.send(b"login")

responce = client.recv(4096)

print(responce.decode())
client.close()
