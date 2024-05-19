import socket

def start_server(host='localhost', port=12345):
    server_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    server_socket.bind((host, port))
    server_socket.listen(1)
    print(f"Server listening on {host}:{port}")
    
    client_socket, addr = server_socket.accept()
    print(f"Connection from {addr}")
    
    while True:
        data = client_socket.recv(1024).decode()
        if data.lower() == 'bye':
            print("Client said bye. Closing connection.")
            client_socket.send("Goodbye!".encode())
            break
        print(f"Client: {data}")
        response = input("Server: ")
        client_socket.send(response.encode())
        if response.lower() == 'bye':
            print("Server said bye. Closing connection.")
            break
    
    client_socket.close()
    server_socket.close()

if __name__ == "__main__":
    start_server()
