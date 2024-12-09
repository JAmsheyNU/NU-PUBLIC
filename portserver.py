import socket

def start_server():
    host = '127.0.0.1'  # Localhost
    port = 12345        # Port number

    try:
        server_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
        server_socket.bind((host, port))
        server_socket.listen(5)
        print(f"Server listening on {host}:{port}...")

        while True:
            client_socket, client_address = server_socket.accept()
            print(f"Connection established with {client_address}")

            message = client_socket.recv(1024).decode('utf-8')
            print(f"Received from client: {message}")
            client_socket.send("Message received".encode('utf-8'))

            client_socket.close()
            print(f"Connection with {client_address} closed.")
    except Exception as e:
        print(f"Error: {e}")
    finally:
        server_socket.close()

if __name__ == "__main__":
    start_server()
