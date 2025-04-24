import socket

HOST = '127.0.0.1'
PORT = 65432

def connect_to_server():
    with socket.socket(socket.AF_INET, socket.SOCK_STREAM) as s:
        s.connect((HOST, PORT))
        message = "Hello from client!"
        s.sendall(message.encode())
        data = s.recv(1024)
        print("Server says:", data.decode())

if __name__ == "__main__":
    connect_to_server()
