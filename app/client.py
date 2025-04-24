import socket
import json

HOST = '127.0.0.1'
PORT = 65432

def send_request(action, username, password):
    data = {
        'action': action,
        'username': username,
        'password': password
    }
    with socket.socket(socket.AF_INET, socket.SOCK_STREAM) as s:
        s.connect((HOST, PORT))
        s.sendall(json.dumps(data).encode())
        response = s.recv(1024)
        print("Server:", response.decode())

if __name__ == "__main__":
    print("1: Register\n2: Login")
    choice = input("Choose option: ")
    username = input("Username: ")
    password = input("Password: ")
    action = 'register' if choice == '1' else 'login'
    send_request(action, username, password)
