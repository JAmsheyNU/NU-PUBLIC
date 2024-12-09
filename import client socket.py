import socket

def connect_to_server():
    host = '127.0.0.1'  # Server address
    port = 12345        # Server port

    try:
        client_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
        client_socket.connect((host, port))
        print(f"Connected to server at {host}:{port}")

        message = "Hello, Server!"
        client_socket.send(message.encode('utf-8'))

        response = client_socket.recv(1024).decode('utf-8')
        print(f"Received from server: {response}")

        client_socket.close()
        print("Disconnected from server.")
    except Exception as e:
        print(f"Error: {e}")

if __name__ == "__main__":
    connect_to_server()
