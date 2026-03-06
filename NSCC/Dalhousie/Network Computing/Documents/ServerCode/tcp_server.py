import socket

TCP_IP = "0.0.0.0"  # Listen on all interfaces
TCP_PORT = 5005

server_sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
server_sock.bind((TCP_IP, TCP_PORT))
server_sock.listen(10)  # Allow up to 5 clients in queue

print(f"TCP Server listening on port {TCP_PORT}...")

while True:
    conn, addr = server_sock.accept()
    print(f"Connection from {addr}")
    
    data = conn.recv(1024).decode()
    print(f"Received: {data}")

    if data.strip().lower() == "hello":
        conn.sendall(b"Hello, TCP Client!")
    
    conn.close()
