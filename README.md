# Flask-Auth-via-Sockets 🔒

A lightweight authentication system combining Flask web interface and secure socket communication.

## Features
- User registration/login via web forms
- SSL-encrypted socket communication
- Password hashing (SHA-256)
- Session management with Flask-Login
- JSON-based user storage

## Requirements
- Python 3.7+
- OpenSSL (for certificate generation)

## Installation
1. Clone repository:
```bash
git clone https://github.com/yourusername/Flask-Auth-via-Sockets.git
cd Flask-Auth-via-Sockets
```

2. Install dependencies:
```bash
pip install -r requirements.txt
```

3. Generate SSL certificates (if needed):
```bash
mkdir server/certs
openssl req -x509 -newkey rsa:4096 -nodes -out server/certs/server.crt -keyout server/certs/server.key -days 365
```

## Usage
1. Start the socket server (in separate terminal):
```bash
python server/server.py
```

2. Start Flask application:
```bash
python app/app.py
```

3. Access in browser:
```
http://localhost:5000
```

## Project Structure
```
├── app/                 - Flask web application
│   ├── templates/       - HTML templates
│   ├── app.py           - Main Flask application
│   └── client.py        - Socket client helper
│
├── server/              
│   ├── certs/           - SSL certificates
│   ├── auth_handler.py  - User authentication logic
│   └── server.py        - SSL socket server
│
└── requirements.txt     - Python dependencies
```


**Authors**  
[Asim Majeed](https://github.com/asimajeed) | [Muhammad Muzammil](https://github.com/MuhammadMuzammil21)