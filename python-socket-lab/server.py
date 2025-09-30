# python
# Import socket library
import socket
# Create TCP/IP socket
s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
# Bind to localhost:8080
s.bind(('localhost', 8080))
# Listen for connections
s.listen(1)
# While True:
# - Accept client connection
# - Receive data from client
# - Process data
# - Send response back
while True:
    conn, addr = s.accept()
    data = conn.recv(1024)
    print(data)
    conn.send(b'Hello, World!')
    conn.close()