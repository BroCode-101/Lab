import socket

# Create a socket object for the client
client_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)

# Connect to the server on localhost and port 8080
client_socket.connect(('localhost', 8080))

# Define the message to send to the server
message = "Hello, I'm Client"
client_socket.send(message.encode())

# Receive the server's response
response = client_socket.recv(1024).decode()
print(f'Received: {response}')

# Close the socket connection
client_socket.close()
