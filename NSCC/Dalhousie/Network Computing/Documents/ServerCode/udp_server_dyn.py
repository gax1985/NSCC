import socket
import random

MAIN_PORT = 6006
SECRET_FLAG = "flag{udp_fun}"

# Main UDP server
main_sock = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
main_sock.bind(("0.0.0.0", MAIN_PORT))

print(f"UDP Server listening on port {MAIN_PORT}...")

while True:
    data, addr = main_sock.recvfrom(1024)
    message = data.decode().strip()
    print(f"Received from {addr}: {message}")

    if message == "start":
        new_port = random.randint(7000, 8000)
        response = f"Send 'retrieve' to port {new_port}."
        main_sock.sendto(response.encode(), addr)

        # Temporary UDP server for this student
        temp_sock = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
        temp_sock.bind(("0.0.0.0", new_port))

        print(f"Temporary server on port {new_port} for {addr}.")

        # Wait for the student to send "retrieve"
        temp_data, temp_addr = temp_sock.recvfrom(1024)

        if temp_data.decode().strip() == "retrieve":
            print(f"Sending flag to {temp_addr}")
            temp_sock.sendto(SECRET_FLAG.encode(), temp_addr)

        # Close the temporary server immediately
        temp_sock.close()
        print(f"Closed temporary server on port {new_port}.")
