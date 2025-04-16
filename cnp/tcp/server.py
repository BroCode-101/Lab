import socket

server_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)

server_socket.bind(('localhost', 12345))

server_socket.listen(5)
print("Server is listening...")

while True:

    client_socket, client_address = server_socket.accept()
    print(f"Connection established with {client_address}")
    
    data = client_socket.recv(1024).decode()
    print(f"Received: {data}")
    
    response = "Hello, Client!"
    client_socket.send(response.encode())
    
    client_socket.close()
