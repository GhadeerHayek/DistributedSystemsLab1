# python
# Import socket library
import socket
# Create TCP/IP socket
s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
# Bind to localhost:8080
# localhost will get the server to accept the connections from the server itself
# 0.0.0.0 will get the client to access the server.
s.bind(('0.0.0.0', 8080))
# Listen for connections
s.listen(1)
# While True:
# - Accept client connection
# - Receive data from client
# - Process data
# - Send response back
while True:
    print('Waiting for connection...')
    conn, addr = s.accept()
    with conn:
        print('Connected by', addr)
        data = conn.recv(1024)
        print("client said: ", data)
        # Now send the response
        conn.sendall(b'Hello, World! I got your message.')
