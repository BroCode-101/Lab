import socket

# Create a socket object
server_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)

# Bind the socket to an address and port
server_socket.bind(('localhost', 8080))

# Listen for incoming connections
server_socket.listen(5)
print("Server is listening...")

while True:
    # Accept a client connection
    client_socket, client_address = server_socket.accept()
    print(f"Connection established with {client_address}")
    
    # Receive data from the client
    data = client_socket.recv(1024).decode()
    print(f"Received: {data}")
    
    # Send data back to the client
    response = "Hello, Client!"
    client_socket.send(response.encode())
    
    # Close the client connection
    client_socket.close()
