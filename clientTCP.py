import socket

HOST = 'localhost'
PORT = int(input("Masukkan port server: "))

client_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM) 

client_socket.connect((HOST, PORT))
print(f"[Client] Terhubung ke {HOST}:{PORT}")

try:
    while True:
        alvian = input("[Client] Ketik pesan: ")
        client_socket.send(alvian.encode('utf-8'))
        data = client_socket.recv(1024)
        if not data:
            print("[Client] Server putus koneksi")
            break

        print(f"[Server] {data.decode('utf-8')}")

        if alvian.lower() in ('exit', 'quit'):
            print("[Client] Keluar chat")
            break

finally:
    client_socket.close()
