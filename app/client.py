import socket, ssl, json

HOST = '127.0.0.1'
PORT = 65432

def send_request_secure(action, username, password):
    data = {
        'action': action,
        'username': username,
        'password': password
    }

    context = ssl.create_default_context()
    context.check_hostname = False
    context.verify_mode = ssl.CERT_NONE  

    with socket.create_connection((HOST, PORT)) as sock:
        with context.wrap_socket(sock, server_hostname=HOST) as ssock:
            try:
                ssock.sendall(json.dumps(data).encode())
                response = ssock.recv(1024)
                response = ssock.recv(1024)
                decoded_response = response.decode()
                print("Server (SSL):", decoded_response)
                return decoded_response
            except Exception as e:
                print("Error communicating with socket server:", e)
                return None

if __name__ == "__main__":
    print("1: Register\n2: Login")
    choice = input("Choose option: ")
    username = input("Username: ")
    password = input("Password: ")
    action = 'register' if choice == '1' else 'login'
    send_request_secure(action, username, password)
