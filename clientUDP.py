import socket

HOST = 'localhost'
PORT = int(input("Masukkan port server (UDP): "))

client_socket = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)

print(f"[Client] Siap mengirim pesan ke {HOST}:{PORT}")

try:
    while True:
        msg = input("[Client] Ketik pesan: ")
        client_socket.sendto(msg.encode(), (HOST, PORT))

        if msg.lower() in ('exit', 'quit'):
            print("[Client] Keluar dari chat")
            break

        data, _ = client_socket.recvfrom(1024)
        print(f"[Server] {data.decode()}")

finally:
    client_socket.close()

