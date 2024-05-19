import socket

def start_client(host='localhost', port=12345):
    client_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    client_socket.connect((host, port))
    
    while True:
        message = input("Client: ")
        client_socket.send(message.encode())
        if message.lower() == 'bye':
            print("Client said bye. Closing connection.")
            break
        data = client_socket.recv(1024).decode()
        if data.lower() == 'bye':
            print("Server said bye. Closing connection.")
            break
        print(f"Server: {data}")
    
    client_socket.close()

if __name__ == "__main__":
    start_client()
