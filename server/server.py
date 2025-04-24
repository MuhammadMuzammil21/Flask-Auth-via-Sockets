import socket
import json
from auth_handler import register_user, validate_user

HOST = '127.0.0.1'
PORT = 65432

def start_server():
    with socket.socket(socket.AF_INET, socket.SOCK_STREAM) as s:
        s.bind((HOST, PORT))
        s.listen()
        print(f"Server listening on {HOST}:{PORT}")
        conn, addr = s.accept()
        with conn:
            print(f"Connected by {addr}")
            data = conn.recv(1024).decode()
            try:
                request = json.loads(data)
                action = request['action']
                username = request['username']
                password = request['password']

                if action == 'register':
                    success = register_user(username, password)
                    response = "Registration successful." if success else "User already exists."
                elif action == 'login':
                    success = validate_user(username, password)
                    response = "Login successful." if success else "Invalid credentials."
                else:
                    response = "Unknown action."

                conn.sendall(response.encode())
            except Exception as e:
                conn.sendall(f"Error: {str(e)}".encode())

if __name__ == "__main__":
    start_server()
