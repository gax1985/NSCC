import socket
import subprocess
import threading

TCP_PORT = 6006

# Function to handle each client separately
def handle_client(conn, addr):
    print(f"New connection from {addr}")

    while True:
        try:
            data = conn.recv(1024).decode().strip()
            if not data:
                break  # If no data, close connection

            print(f"Received from {addr}: {data}")

            if data.lower() == "bye":
                conn.sendall(b"Goodbye! Connection closing.")
                break  # Exit loop to close connection

            # Run the `fortune` command and capture output
            fortune = subprocess.run(["fortune"], capture_output=True, text=True).stdout.strip()

            # Send the generated fortune message
            conn.sendall(fortune.encode())

        except ConnectionResetError:
            print(f"Connection lost with {addr}")
            break

    conn.close()
    print(f"Connection with {addr} closed.")

# Create a TCP server socket
server_sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
server_sock.bind(("0.0.0.0", TCP_PORT))
server_sock.listen(10)  # Allow up to 10 students to connect at once

print(f"Multi-threaded TCP Fortune Server listening on port {TCP_PORT}...")

while True:
    conn, addr = server_sock.accept()
    # Start a new thread for each client
    client_thread = threading.Thread(target=handle_client, args=(conn, addr))
    client_thread.start()
