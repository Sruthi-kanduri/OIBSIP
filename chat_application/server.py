import socket
import threading

# Function to handle client connections
def handle_client(client_socket, clients):
    while True:
        try:
            message = client_socket.recv(1024).decode('utf-8')
            if message:
                broadcast(message, client_socket, clients)
            else:
                remove(client_socket, clients)
        except:
            continue

# Function to broadcast messages to all clients
def broadcast(message, client_socket, clients):
    for client in clients:
        if client != client_socket:
            try:
                client.send(message.encode('utf-8'))
            except:
                remove(client, clients)

# Function to remove clients that have disconnected
def remove(client_socket, clients):
    if client_socket in clients:
        clients.remove(client_socket)

def main():
    server = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    server.bind(('192.168.2.22', 5555))
    server.listen(5)
    clients = []

    print("Server started. Waiting for connections...")

    while True:
        client_socket, addr = server.accept()
        clients.append(client_socket)
        print(f"Connection from {addr}")

        threading.Thread(target=handle_client, args=(client_socket, clients)).start()

if __name__ == "__main__":
    main()