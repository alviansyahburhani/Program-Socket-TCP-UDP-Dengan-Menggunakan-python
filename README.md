📡 Laporan Pemrograman Jaringan

"Pembuatan Socket TCP/UDP dengan Python"

👨‍💻 Oleh:

Alvian Syah BurhaniNIM: 105841103522

👨‍🏫 Dosen Pembimbing:

Ir. Runal Rezkiawan, S.Kom., M.T., IPP.NIDN: 0904019301

Program Studi S1 Informatika – Fakultas TeknikUniversitas Muhammadiyah Makassar2025

🕌 Kata Pengantar

Segala puji bagi Allah SWT atas segala kemudahan dan kesehatan yang diberikan sehingga saya dapat menyelesaikan laporan ini dengan baik. Saya juga mengucapkan terima kasih kepada dosen pembimbing, serta semua pihak yang telah membantu selama proses pengerjaan tugas ini. Semoga laporan ini dapat memberikan manfaat bagi pembaca.

Makassar, 25 Maret 2025Alvian Syah Burhani

📖 BAB I – PENDAHULUAN

🔎 Latar Belakang

Perkembangan teknologi komputer telah memungkinkan komunikasi data yang efisien. Salah satunya adalah penggunaan socket dalam pemrograman jaringan, baik berbasis TCP (reliable) maupun UDP (unreliable). Python menyediakan modul socket yang memudahkan pengembangan aplikasi jaringan.

Dalam tugas ini, saya diminta membuat dua jenis socket — TCP dan UDP — masing-masing dengan dua komponen utama: server dan client.

🎯 Tujuan

Mengimplementasikan socket TCP dan UDP menggunakan Python.

Mengetahui perbedaan komunikasi antara TCP dan UDP.

Menyusun skema komunikasi untuk masing-masing socket.

Mempersonalisasi program dengan menggunakan nama variabel alvian.

🧠 BAB II – PEMBAHASAN

📚 Dasar Teori

Dalam pemrograman jaringan menggunakan Python, komunikasi antar proses dapat dilakukan melalui modul socket, yang menyediakan antarmuka untuk membuat dan mengelola koneksi jaringan.

Python mendukung dua domain komunikasi utama:
•	AF_UNIX digunakan untuk komunikasi lokal (antar proses dalam satu sistem) dan pengalamatan dilakukan melalui local path seperti /tmp/sock.
•	AF_INET digunakan untuk komunikasi jaringan berbasis protokol 
Internet, dan pengalamatan dilakukan menggunakan tuple (host, port).

Dalam program yang dibuat, digunakan domain AF_INET, karena komunikasi yang dilakukan adalah antara server dan client melalui jaringan (meskipun menggunakan alamat lokal localhost). Port yang digunakan dalam program ini dipilih di atas angka 1024 untuk menghindari konflik dengan port sistem yang memerlukan akses administratif.

Sebelum menggunakan socket, modul socket harus diimpor terlebih dahulu:
 
Setelah modul diimpor, socket dibuat menggunakan perintah berikut:
 

Jenis socket yang digunakan ditentukan oleh parameternya:
•	SOCK_STREAM: untuk protokol TCP. Koneksi bersifat andal dan menjamin urutan pengiriman data.
•	SOCK_DGRAM: untuk protokol UDP. Koneksi bersifat ringan, cepat, namun tidak menjamin keandalan dan urutan pengiriman.
a)	Binding
Binding adalah proses mengikat socket server ke alamat IP dan nomor port tertentu agar dapat menerima koneksi masuk. Dilakukan dengan perintah:
 
b)	Listening dan Accepting (TCP)
Untuk komunikasi berbasis TCP, setelah binding, server perlu mendengarkan koneksi masuk dan menerima koneksi client
 
Yang artinya pertama server akan akan mendengarkan permintaan terhubung dan 1 itu akan membatasi jumlah maksismum antrean koneksi, Dan accept akan menerima koneksi dan mengembalikan socket baru dan Alamat client
c)	   Sanding dan Receiving
Untuk pertukaran data, TCP dan UDP memiliki fungsi berbeda tergantung pada protokol yang digunakan :
•	TCP
 
Send digunakan mengirim data ke pihak lain melalui koneksi TCP yang telah terbentuk.data harus dalam format byte, sehingga biasanya dilakukan encoding terlebih dahulu 
recv(buffer_size) Digunakan untuk menerima data dari pihak lain dan dibatsi dengan jumlah maksimum byte yang ingin dibaca dalam satu kali panggilan

•	UDP
 
sendto(data, address) Digunakan untuk mengirim data ke alamat tertentu (tanpa koneksi tetap)
recvfrom(buffer_size) Digunakan untuk menerima data dan mendapatkan informasi alamat pengirim.

d)	Closing
Untuk mengakhiri koneksi dan membebaskan resource sistem, socket harus ditutup dengan:
 
Hal ini dilakukan baik di sisi client maupun server setelah komunikasi selesai atau jika terjadi kesalahan.


🧪 Implementasi Program

🔁 TCP (Transmission Control Protocol)
Socket TCP (Transmission Control Protocol) adalah protokol connection-oriented, artinya sebelum data dikirimkan, harus ada koneksi yang dibentuk terlebih dahulu antara client dan server. Protokol ini menjamin keutuhan dan urutan data yang dikirim.

📄 Kode: ServerTCP.py
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

📝 Penjelasan: kode :
•	Server menggunakan localhost dan port dari input pengguna.
•	Socket dibuat dengan AF_INET dan SOCK_STREAM (untuk TCP).
•	Server mendengarkan koneksi dengan listen(1) dan menerima client dengan accept().
•	Server terus menerima pesan dari client (recv), menampilkannya, dan membalas dengan send.
•	Jika client mengirim 'exit' atau 'quit', koneksi ditutup dengan close().

📄 Kode: ClientTCP.py
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

📝 Penjelasan kode :
•	Client terhubung ke server di localhost dan port dari input pengguna.
•	Socket dibuat dengan AF_INET dan SOCK_STREAM (untuk menandakan bahawa TCP).
•	Client mengirim pesan ke server menggunakan send().
•	Setelah mengirim, client menunggu balasan dari server dengan recv().
•	Jika mengetik 'exit' atau 'quit', client keluar dari chat dan koneksi ditutup dengan close().


🚀 UDP (User Datagram Protocol)
Socket UDP (User Datagram Protocol) adalah protokol connectionless yang lebih ringan dibandingkan TCP. Pengiriman data menggunakan UDP tidak memerlukan koneksi awal, sehingga lebih cepat tetapi tidak menjamin data sampai dengan urut dan utuh.

📄 Kode: ServerUDP.py
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

📝 Penjelasan Kode:
•	server UDP dibuat menggunakan socket.SOCK_DGRAM
•	Server di-bind ke alamat dan port yang dimasukkan.
•	Server siap menerima pesan dari client dengan recvfrom().
•	Data dan alamat client diterima yang telah di decode, lalu pesan ditampilkan di terminal.
•	Jika pesan client adalah 'exit' atau 'quit', maka server keluar dari chat.
•	Server meminta input balasan dari user dan mengirimkannya ke client dengan sendto().
•	Jika server mengetik 'exit' atau 'quit', maka server keluar dari chat.
•	Setelah keluar dari chat, socket ditutup dengan close().

📄 Kode: ClientUDP.py

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

📝 Penjelasan kode :
•	Client terhubung ke alamat host (localhost) dan port yang dimasukkan oleh pengguna.
•	Socket dibuat dengan tipe UDP (SOCK_DGRAM) menggunakan socket.socket(socket.AF_INET, socket.SOCK_DGRAM).
•	Setelah socket berhasil dibuat, client siap mengirim pesan ke server (ditampilkan melalui print).
•	Di dalam loop while True, client akan:
•	Meminta input pesan dari pengguna (input("[Client] Ketik pesan: ")).
•	Mengirim pesan ke server menggunakan sendto() ke alamat (HOST, PORT).
•	Jika pesan yang diketik adalah "exit" atau "quit", maka client keluar dari chat dan loop dihentikan.
•	Setelah mengirim pesan, client menunggu balasan dari server menggunakan recvfrom(6).
•	Pesan dari server kemudian ditampilkan ke layar.
•	Setelah keluar dari loop, koneksi socket ditutup dengan client_socket.close().

🧭 Skema Komunikasi
Skema TCP:
![image](https://github.com/user-attachments/assets/064a6485-1622-4106-b3ca-f690ce706f80)

Skema UDP:
![image](https://github.com/user-attachments/assets/a4a006b7-a743-477a-a136-3c2dcbe17700)


🛠️ Hasil Asistensi & Perubahan
Berdasarkan hasil asistensi yang telah dilakukan bersama dosen pengampu, terdapat dua poin penting yang diminta untuk diperbaiki atau ditambahkan dalam tugas implementasi socket TCP dan UDP. Adapun kedua poin tersebut adalah sebagai berikut:

Skema komunikasi ditambahkan sesuai arahan dosen.
Dosen meminta agar disusun skema komunikasi untuk masing-masing implementasi socket, baik TCP maupun UDP. Skema ini bertujuan untuk menjelaskan secara sistematis alur proses komunikasi antara server dan client. Permintaan ini telah ditindaklanjuti dengan menyusun skema yang ditampilkan secara rinci pada Bagian C: Skema Komunikasi TCP dan UDP, yang menggambarkan proses pengiriman dan penerimaan pesan dari kedua sisi secara jelas.

Variabel msg.encode() diganti menjadi alvian.encode() sebagai personalisasi.
Selain perubahan pada variabel data, dosen juga mengarahkan agar nama variabel yang sebelumnya menggunakan msg.encode() diubah menjadi alvian.encode(). Modifikasi ini diterapkan pada bagian kode yang menangani proses pengiriman pesan dari client ke server maupun sebaliknya, baik dalam implementasi TCP maupun UDP. Perubahan ini menunjukkan kemampuan dalam memodifikasi dan memahami proses encoding data dalam komunikasi socket.


✅ BAB III – PENUTUP

📝 Kesimpulan

Melalui tugas ini, saya memahami:

Perbedaan TCP dan UDP secara teknis dan implementasi.

Membangun socket client-server menggunakan Python.

Mengatur encoding, koneksi, pengiriman data, dan menutup socket dengan baik.

Dengan tambahan asistensi, saya menyusun skema komunikasi yang memudahkan pemahaman dan memodifikasi kode dengan identitas pembuat.

📎 Lampiran

📂 Kode Program tersedia di:Google Drive Folder

📚 Daftar Pustaka

Gunawan, R. (2007). Pemrograman socket dengan Python. IlmuKomputer.Com.

Listiyono, E. dkk. (2009). Jaringan komputer dan komunikasi data. Graha Ilmu.

Van Rossum, G. (2002). Python documentation (Release 2.2.2). Python.org

Raven, P. H. dkk. (2015). Biology (10th ed.). McGraw-Hill Education.




