import socket

HOST = 'localhost'
PORT = int(input("Masukkan port server: "))

server_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
server_socket.bind((HOST, PORT))
server_socket.listen(1)
print(f"[Server] Menunggu koneksi di {HOST}:{PORT}…")

client_socket, addr = server_socket.accept()
print(f"[Server] Terhubung dengan {addr}")

try:
    while True:
        data = client_socket.recv(1024)
        if not data:
            print("[Server] Client putus koneksi")
            break

        print(f"[Client] {data.decode()}")
        reply = input("[Server] Ketik balasan: ")
        client_socket.send(reply.encode())
        
        if data.decode().lower() in ('exit', 'quit'):
            print("[Server] Client keluar dari chat")
            break

finally:
    client_socket.close()
    server_socket.close()
