import socket
import threading

# Function to handle receiving messages from the server
def receive_messages(client_socket):
    while True:
        try:
            message = client_socket.recv(1024).decode('utf-8')
            if message:
                print(message)
        except:
            print("An error occurred!")
            client_socket.close()
            break

def main():
    client = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    server_address = input("Enter server IP address: ")
    client.connect((server_address, 5555))

    # Start a thread to receive messages from the server
    threading.Thread(target=receive_messages, args=(client,)).start()

    # Send messages to the server
    while True:
        message = input("")
        if message:
            client.send(message.encode('utf-8'))

if __name__ == "__main__":
    main()