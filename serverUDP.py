import socket

HOST = 'localhost'
PORT = int(input("Masukkan port server (UDP): "))


server_socket = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
server_socket.bind((HOST, PORT))

print(f"[Server] Menunggu pesan di {HOST}:{PORT}…")

try:
    while True:
        data, addr = server_socket.recvfrom(1024)
        print(f"[Client {addr}] {data.decode()}")

        if data.decode().lower() in ('exit', 'quit'):
            print("[Server] Client keluar dari chat")
            break

        reply = input("[Server] Ketik balasan: ")
        server_socket.sendto(reply.encode(), addr)

        if reply.lower() in ('exit', 'quit'):
            print("[Server] Server keluar dari chat")
            break

finally:
    server_socket.close()

