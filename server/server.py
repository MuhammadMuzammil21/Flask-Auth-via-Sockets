import socket, ssl, json
from auth_handler import register_user, validate_user

HOST = '127.0.0.1'
PORT = 65432
CERT_FILE = 'server/certs/server.crt'
KEY_FILE = 'server/certs/server.key'

def start_secure_server():
    context = ssl.SSLContext(ssl.PROTOCOL_TLS_SERVER)
    context.load_cert_chain(certfile=CERT_FILE, keyfile=KEY_FILE)

    with socket.socket(socket.AF_INET, socket.SOCK_STREAM) as sock:
        sock.bind((HOST, PORT))
        sock.listen(5)
        print(f"[SSL] Secure server listening on {HOST}:{PORT}")
        with context.wrap_socket(sock, server_side=True) as ssock:
            conn, addr = ssock.accept()
            with conn:
                print(f"[SSL] Connection from {addr}")
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
    start_secure_server()
