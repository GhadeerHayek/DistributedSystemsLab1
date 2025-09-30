# the client will be connecting to the server on the designated port
# it will send a message and print the response

import socket

client_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
# the port to connect is the same as the port to bind in the server file
client_socket.connect(('localhost', 8080))
# the string must be encoded to bytes
message = 'Hello, World! I am testing the socket.'
message_encoded = message.encode('utf-8')
print("trying to send a message:", message)
client_socket.sendall(message_encoded)
# print the response
response = client_socket.recv(1024)
print("server said: ", response)
# close connection
client_socket.close()
