📡 Laporan Pemrograman Jaringan
Pembuatan Socket TCP/UDP dengan Python
👨‍💻 Oleh
Alvian Syah Burhani
NIM: 105841103522

👨‍🏫 Dosen Pembimbing
Ir. Runal Rezkiawan, S.Kom., M.T., IPP
NIDN: 0904019301

Program Studi S1 Informatika – Fakultas Teknik
Universitas Muhammadiyah Makassar
2025

🕌 Kata Pengantar
Segala puji bagi Allah SWT atas segala kemudahan dan kesehatan yang diberikan sehingga saya dapat menyelesaikan laporan ini dengan baik. Saya juga mengucapkan terima kasih kepada dosen pembimbing, serta semua pihak yang telah membantu selama proses pengerjaan tugas ini. Semoga laporan ini dapat memberikan manfaat bagi pembaca.

Makassar, 25 Maret 2025
Alvian Syah Burhani

📖 BAB I – PENDAHULUAN
🔎 Latar Belakang
Perkembangan teknologi komputer telah memungkinkan komunikasi data yang efisien. Salah satunya adalah penggunaan socket dalam pemrograman jaringan, baik berbasis TCP (reliable) maupun UDP (unreliable). Python menyediakan modul socket yang memudahkan pengembangan aplikasi jaringan.

Dalam tugas ini, saya diminta membuat dua jenis socket — TCP dan UDP, masing-masing dengan dua komponen utama: server dan client.

🎯 Tujuan
Mengimplementasikan socket TCP dan UDP menggunakan Python.

Mengetahui perbedaan komunikasi antara TCP dan UDP.

Menyusun skema komunikasi untuk masing-masing socket.

Mempersonalisasi program dengan menggunakan nama variabel alvian.

🧠 BAB II – PEMBAHASAN
📚 Dasar Teori
Dalam pemrograman jaringan menggunakan Python, komunikasi antar proses dapat dilakukan melalui modul socket, yang menyediakan antarmuka untuk membuat dan mengelola koneksi jaringan.

Python mendukung dua domain komunikasi utama:

AF_UNIX digunakan untuk komunikasi lokal (antar proses dalam satu sistem) dan pengalamatan dilakukan melalui local path seperti /tmp/sock.

AF_INET digunakan untuk komunikasi jaringan berbasis protokol Internet, dan pengalamatan dilakukan menggunakan tuple (host, port).

Dalam program yang dibuat, digunakan domain AF_INET, karena komunikasi dilakukan antara server dan client melalui jaringan (meskipun menggunakan alamat lokal localhost). Port yang digunakan dipilih di atas angka 1024 untuk menghindari konflik dengan port sistem.

Sebelum menggunakan socket, modul socket harus diimpor terlebih dahulu.

Jenis socket yang digunakan ditentukan oleh parameternya:
SOCK_STREAM: untuk protokol TCP. Koneksi andal dan menjamin urutan data.

SOCK_DGRAM: untuk protokol UDP. Koneksi ringan dan cepat, namun tidak menjamin keandalan.

a) Binding
Binding adalah proses mengikat socket server ke alamat IP dan port agar dapat menerima koneksi masuk.

b) Listening dan Accepting (TCP)
Server mendengarkan koneksi masuk dan menerima koneksi dari client. Fungsi accept() akan mengembalikan socket baru dan alamat client.

c) Sending dan Receiving
Untuk pertukaran data, TCP dan UDP memiliki fungsi berbeda:

TCP:

send() mengirim data (harus dalam bentuk byte, dilakukan encode() terlebih dahulu).

recv() menerima data dari pihak lain.

UDP:

sendto(data, address) mengirim data ke alamat tertentu.

recvfrom(buffer_size) menerima data sekaligus alamat pengirim.

d) Closing
Untuk mengakhiri koneksi dan membebaskan resource sistem, socket harus ditutup baik di sisi client maupun server.

🧪 Implementasi Program
🔁 TCP (Transmission Control Protocol)
📄 ServerTCP.py
Kode program untuk server TCP.

python
Copy
Edit
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
📝 Penjelasan:
Server menggunakan localhost dan port dari input pengguna. Socket dibuat dengan AF_INET dan SOCK_STREAM, mendengarkan koneksi masuk, menerima pesan, lalu membalas. Socket ditutup saat client mengirim 'exit' atau 'quit'.

📄 ClientTCP.py
Kode program untuk client TCP.

python
Copy
Edit
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
📝 Penjelasan:
Client terhubung ke server, mengirim pesan, dan menerima balasan. Keluar jika mengetik 'exit' atau 'quit'.

🚀 UDP (User Datagram Protocol)
📄 ServerUDP.py
Kode program untuk server UDP.

python
Copy
Edit
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
Kode program untuk client UDP.

python
Copy
Edit
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
📝 Penjelasan:
UDP tidak membutuhkan koneksi awal. Client mengirim pesan dengan sendto(), server menerima dengan recvfrom(), dan membalas menggunakan alamat pengirim.

🧭 Skema Komunikasi
Skema TCP
Client → Connect → Server → Accept
Client ↔ (Send ↔ Receive) ↔ Server
Client → Close ↔ Close ← Server

Skema UDP
Client → sendto() → Server
Server → recvfrom() → Client
Loop hingga exit

🛠️ Hasil Asistensi & Perubahan
Skema komunikasi ditambahkan sesuai permintaan dosen untuk memudahkan pemahaman alur komunikasi.

Variabel msg.encode() diubah menjadi alvian.encode() untuk menunjukkan identitas pembuat program.

✅ BAB III – PENUTUP
📝 Kesimpulan
TCP dan UDP memiliki perbedaan mendasar dalam keandalan dan urutan data.

Socket Python memudahkan implementasi protokol jaringan.

Proyek ini memperkuat pemahaman tentang transport layer dan pemrograman jaringan.

📚 Daftar Pustaka
Gunawan, R. (2007). Pemrograman socket dengan Python. IlmuKomputer.Com.

Listiyono, E., Harjito, I. B., & Susetyo, E. (2009). Jaringan komputer dan komunikasi data. Graha Ilmu.

Van Rossum, G. (2002). Python documentation (Release 2.2.2). Python.org

Raven, P. H., Johnson, G. B., Losos, J. B., & Singer, S. R. (2015). Biology (10th ed.). McGraw-Hill Education.

