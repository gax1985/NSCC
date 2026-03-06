import socket

UDP_IP = "0.0.0.0"  # Listen on all network interfaces
UDP_PORT = 5005  # Change if needed

sock = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
sock.bind((UDP_IP, UDP_PORT))

print(f"UDP server is running on port {UDP_PORT}...")

while True:
    data, addr = sock.recvfrom(1024)  # Receive message
    print(f"Received from {addr}: {data.decode()}")

    # Simple challenge: send "hello" to get the flag
    if data.decode().strip().lower() == "hello":
        response = "flag{welcome to my world!}"
    else:
        response = "Try again! Send 'hello'"

    sock.sendto(response.encode(), addr)  # Send response