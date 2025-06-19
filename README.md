📡 Laporan Pemrograman Jaringan

Pembuatan Socket TCP/UDP dengan Python

👨‍💻 Oleh: Alvian Syah Burhani

🆔 NIM: 105841103522

👨‍🏫 Dosen Pembimbing: Ir. Runal Rezkiawan, S.Kom., M.T., IPP

🔖 NIDN: 0904019301

🎓 Program Studi S1 Informatika – Fakultas Teknik🏛️ Universitas Muhammadiyah Makassar – 2025

🕌 Kata Pengantar

Segala puji bagi Allah SWT atas segala kemudahan dan kesehatan yang diberikan sehingga saya dapat menyelesaikan laporan ini dengan baik. Saya juga mengucapkan terima kasih kepada dosen pembimbing, serta semua pihak yang telah membantu selama proses pengerjaan tugas ini. Semoga laporan ini dapat memberikan manfaat bagi pembaca.

📍 Makassar, 25 Maret 2025✍️ Alvian Syah Burhani

📖 BAB I – PENDAHULUAN

🔎 Latar Belakang

Perkembangan teknologi komputer telah memungkinkan komunikasi data yang efisien. Salah satunya adalah penggunaan socket dalam pemrograman jaringan, baik berbasis TCP (reliable) maupun UDP (unreliable). Python menyediakan modul socket yang memudahkan pengembangan aplikasi jaringan.

Dalam tugas ini, saya diminta membuat dua jenis socket — TCP dan UDP, masing-masing dengan dua komponen utama: server dan client.

🎯 Tujuan

🚀 Mengimplementasikan socket TCP dan UDP menggunakan Python

🔍 Mengetahui perbedaan komunikasi antara TCP dan UDP

📡 Menyusun skema komunikasi untuk masing-masing socket

🧾 Mempersonalisasi program dengan menggunakan nama variabel alvian

🧠 BAB II – PEMBAHASAN

📚 Dasar Teori

AF_INET → komunikasi berbasis IP

SOCK_STREAM → protokol TCP

SOCK_DGRAM → protokol UDP

🛠️ Proses Penting:

Binding: mengaitkan socket ke IP dan port

Listening & Accepting: untuk koneksi TCP

Send & Receive:

TCP → send() / recv()

UDP → sendto() / recvfrom()

Closing: menutup socket untuk membebaskan resource

🧪 Implementasi Program

🔁 TCP (Transmission Control Protocol)

📄 ServerTCP.py

import socket
host = '127.0.0.1'
port = int(input("Masukkan port server: "))
server_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
server_socket.bind((host, port))
server_socket.listen(1)
print("Menunggu koneksi dari client...")
client_socket, addr = server_socket.accept()
print(f"Terhubung dengan {addr}")
while True:
    alvian = client_socket.recv(1024).decode()
    if alvian.lower() in ["exit", "quit"]:
        break
    print(f"[Client]: {alvian}")
    balas = input("[Server] Ketik balasan: ")
    client_socket.send(balas.encode())
client_socket.close()
server_socket.close()

📌 Penjelasan

Membuat koneksi TCP (reliable)

Terima pesan dari client

Kirim balasan

Akhiri koneksi dengan close()

📄 ClientTCP.py

import socket
host = '127.0.0.1'
port = int(input("Masukkan port server: "))
client_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
client_socket.connect((host, port))
while True:
    alvian = input("[Client] Ketik pesan: ")
    client_socket.send(alvian.encode())
    if alvian.lower() in ["exit", "quit"]:
        break
    data = client_socket.recv(1024).decode()
    print(f"[Server]: {data}")
client_socket.close()

📌 Penjelasan

Kirim pesan ke server

Terima balasan

Keluar jika mengetik exit / quit

🚀 UDP (User Datagram Protocol)

📄 ServerUDP.py

import socket
host = '127.0.0.1'
port = int(input("Masukkan port server: "))
server_socket = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
server_socket.bind((host, port))
while True:
    alvian, addr = server_socket.recvfrom(1024)
    alvian = alvian.decode()
    if alvian.lower() in ["exit", "quit"]:
        break
    print(f"[Client]: {alvian}")
    balas = input("[Server] Ketik balasan: ")
    server_socket.sendto(balas.encode(), addr)
server_socket.close()

📄 ClientUDP.py

import socket
host = '127.0.0.1'
port = int(input("Masukkan port server: "))
client_socket = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
while True:
    alvian = input("[Client] Ketik pesan: ")
    client_socket.sendto(alvian.encode(), (host, port))
    if alvian.lower() in ["exit", "quit"]:
        break
    data, _ = client_socket.recvfrom(1024)
    print(f"[Server]: {data.decode()}")
client_socket.close()

📌 Penjelasan

Protokol connectionless

Tidak menjamin urutan & keutuhan data

Kirim langsung ke IP dan port tanpa handshake

🧭 Skema Komunikasi

🔗 TCP

Client → Connect → Server
Client ↔ (Send ↔ Receive) ↔ Server
Client → Close ← Server

📡 UDP

Client → SendTo → Server
Server → RecvFrom → Client
Tanpa koneksi tetap, langsung kirim-balas

🛠️ Hasil Asistensi & Perubahan

📌 Tindak lanjut hasil asistensi:

✅ Ditambahkan skema komunikasi TCP dan UDP secara eksplisit

✅ Variabel msg.encode() diganti menjadi alvian.encode() untuk personalisasi kode

✅ BAB III – PENUTUP

📝 Kesimpulan

Melalui tugas ini, saya:

Memahami perbedaan protokol TCP dan UDP

Mengembangkan program client-server menggunakan Python dan modul socket

Memodifikasi kode secara personal dan menyesuaikan struktur logika komunikasi jaringan

📚 Daftar Pustaka

Gunawan, R. (2007). Pemrograman socket dengan Python. IlmuKomputer.Com.

Listiyono, E. dkk. (2009). Jaringan komputer dan komunikasi data. Graha Ilmu.

Van Rossum, G. (2002). Python documentation (Release 2.2.2). Python.org

Raven, P. H. dkk. (2015). Biology (10th ed.). McGraw-Hill Education.
