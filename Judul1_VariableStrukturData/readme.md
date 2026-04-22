A. Judul Program

Sistem Pemesanan Kursi Bioskop Menggunakan List 2 Dimensi

B. Deskripsi Singkat

Program ini dibuat untuk mensimulasikan pemesanan kursi di bioskop. Di dalam program ini, kursi direpresentasikan dalam bentuk list dua dimensi, sehingga tersusun seperti baris dan kolom seperti denah kursi di bioskop pada umumnya.
Pengguna bisa melihat daftar kursi yang masih kosong, memesan kursi tertentu, dan keluar dari program melalui menu yang tersedia. Kursi yang masih kosong ditandai dengan angka 0, sedangkan kursi yang sudah dipesan akan berubah menjadi 1.

Program ini menggunakan perulangan while supaya program tetap berjalan sampai pengguna memilih untuk keluar. Selain itu, digunakan juga percabangan if-elif-else untuk menentukan aksi sesuai dengan pilihan yang dimasukkan oleh pengguna. Untuk menghindari error saat input, program dilengkapi dengan try-except, jadi kalau pengguna salah memasukkan data, program tidak langsung berhenti.

C. Source Code dan Penjelasan

<img width="478" height="116" alt="Cuplikan layar 2026-04-22 182640" src="https://github.com/user-attachments/assets/4458d927-ecd8-4baf-ab74-bc7ec6d4a671" />

Fungsi menu() digunakan untuk menampilkan pilihan menu kepada pengguna/user.

<img width="703" height="85" alt="Cuplikan layar 2026-04-22 183448" src="https://github.com/user-attachments/assets/86ade87d-03fc-4f97-b57e-75ce61d8b140" />
Membuat list 2 dimensi berukuran 3 baris x 2 kolom.
Nilai 0 berarti kursi kosong.

<img width="318" height="30" alt="Cuplikan layar 2026-04-22 183506" src="https://github.com/user-attachments/assets/98cc62be-4227-47de-8966-2acf2842a7d7" />
Variabel untuk mengontrol perulangan program.

<img width="380" height="62" alt="Cuplikan layar 2026-04-22 183526" src="https://github.com/user-attachments/assets/867d1620-e07d-4406-a648-6016c22bc61b" />
Program akan terus berjalan selama running = True.

<img width="600" height="61" alt="Cuplikan layar 2026-04-22 184128" src="https://github.com/user-attachments/assets/704f21d8-d268-4d0e-8b58-75024e286b5a" />
Mengambil input pilihan dari user.

<img width="658" height="81" alt="Cuplikan layar 2026-04-22 183602" src="https://github.com/user-attachments/assets/594bdb98-b48a-4e2f-899f-950b6034b3b4" />
Menangani error jika input bukan angka.

<img width="516" height="68" alt="Cuplikan layar 2026-04-22 183621" src="https://github.com/user-attachments/assets/7253764c-184b-47ed-97db-add3162fe318" />
Jika user memilih 1, program menampilkan kursi.

<img width="681" height="109" alt="Cuplikan layar 2026-04-22 183649" src="https://github.com/user-attachments/assets/a96b1eaa-0725-4b80-b346-a4bdd36af2f7" />
Menampilkan isi list 2 dimensi (denah kursi).

<img width="420" height="33" alt="Cuplikan layar 2026-04-22 184451" src="https://github.com/user-attachments/assets/6d7b8d02-494b-4592-b67f-e760e9b32e54" />
Jika user memilih 2, program masuk ke proses pemesanan kursi.

<img width="765" height="84" alt="Cuplikan layar 2026-04-22 184500" src="https://github.com/user-attachments/assets/e3c2947e-0d7f-4a9a-b552-c3ad43a88bf0" />
Input posisi kursi berdasarkan baris dan kolom.

<img width="700" height="99" alt="Cuplikan layar 2026-04-22 184511" src="https://github.com/user-attachments/assets/1a383f31-d650-41b1-96e3-3b39902786cf" />
Jika kursi kosong (0), maka diubah menjadi 1 (terisi).

<img width="710" height="59" alt="Cuplikan layar 2026-04-22 184521" src="https://github.com/user-attachments/assets/2e56492d-a702-45ab-9ee2-1c08b6bf1ef9" />
Jika kursi sudah dipesan.

<img width="657" height="72" alt="Cuplikan layar 2026-04-22 184528" src="https://github.com/user-attachments/assets/4f0b65f6-69c7-495b-b24b-7696bb453106" />
Menangani error jika input salah atau di luar indeks.

<img width="563" height="97" alt="Cuplikan layar 2026-04-22 184537" src="https://github.com/user-attachments/assets/b5ce1e15-eabe-4336-947b-2d0b965f3252" />
Menghentikan program.

<img width="681" height="73" alt="Cuplikan layar 2026-04-22 184548" src="https://github.com/user-attachments/assets/bcdcb177-1b37-4c30-b0c1-621988bab439" />
Jika pilihan tidak tersedia di menu.

<img width="429" height="79" alt="Cuplikan layar 2026-04-22 185645" src="https://github.com/user-attachments/assets/8ea4579f-e599-459e-b8e6-5ff83d9cf1ec" />
Menjalankan fungsi main() saat program dijalankan.




D. Output Program: 
Program akan menampilkan menu seperti berikut:
<img width="244" height="100" alt="Cuplikan layar 2026-04-22 185822" src="https://github.com/user-attachments/assets/bdabc7e8-d495-42d7-a86d-4f8a5568729e" />
Contoh tampilan denah kursi:
<img width="196" height="104" alt="Cuplikan layar 2026-04-22 190041" src="https://github.com/user-attachments/assets/59bb6ec6-74c9-48e1-8b13-864f944c5afb" />
Setelah memesan kursi:
<img width="266" height="100" alt="Cuplikan layar 2026-04-22 190525" src="https://github.com/user-attachments/assets/b3089a14-6d1d-4516-8d95-af5db6ce8ad0" />
Keterangan:

0 = Kursi kosong

1 = Kursi sudah dipesan

Program akan menolak input yang tidak valid dan memastikan kursi tidak bisa dipesan dua kali.

E. Link YouTube
https://youtu.be/fEiuYi3FisQ?si=5qQCBp_qIGg12B6m
