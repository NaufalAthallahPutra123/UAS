# UAS

## Project UAS Bahasa Pemrograman

## Program Pengolahan Nilai Mahasiswa (OOP & Modular)

## Deskripsi Program

Program ini merupakan aplikasi sederhana berbasis Python yang digunakan untuk mengolah nilai mahasiswa.
Program dibuat dengan menerapkan konsep Object Oriented Programming (OOP) dan modular, sesuai dengan ketentuan Project UAS Bahasa Pemrograman.

Aplikasi mampu menerima input dari pengguna, melakukan validasi data, memproses nilai, dan menampilkan hasil dalam bentuk tampilan terstruktur.

## Tujuan Program

1. Menerapkan konsep OOP dalam pembuatan program

2. Menerapkan modular programming

3. Menggunakan validasi input dan exception handling

4. Menampilkan hasil pengolahan data secara rapi

## Konsep yang Digunakan

1. Object Oriented Programming (OOP)

2. Modular Programming

3. Exception Handling

4. Input & Output Console

## Penjelasan Setiap File Program
1.  mahasiswa.py (Class Data)


<img width="955" height="504" alt="mahasiswa" src="https://github.com/user-attachments/assets/8d774dda-0f82-4e20-978b-7ff601aae790" />


File ini berfungsi sebagai class data yang menyimpan informasi mahasiswa.

Penjelasan:

Class Mahasiswa digunakan untuk merepresentasikan satu objek mahasiswa

Data yang disimpan:

nama → nama mahasiswa

nim → nomor induk mahasiswa

nilai → nilai mahasiswa

Class ini tidak melakukan proses atau tampilan, hanya sebagai penyimpan data

Tujuan penggunaan:

Menerapkan konsep encapsulation

Memisahkan data dari proses dan tampilan

Memudahkan pengelolaan data jika program dikembangkan lebih lanjut

2. proses.py (Class Process)


<img width="955" height="504" alt="proses" src="https://github.com/user-attachments/assets/564229eb-5e6e-4473-8751-e0e86fad2602" />


File ini berfungsi sebagai class proses untuk mengolah data mahasiswa.

Penjelasan:

Class NilaiProcessor berisi logika penilaian

Method tentukan_grade() digunakan untuk:

Mengolah nilai mahasiswa

Menentukan grade berdasarkan rentang nilai

Proses penilaian dipisahkan dari input dan output

Tujuan penggunaan:

Menerapkan konsep single responsibility principle

Memisahkan logika bisnis dari tampilan

Memudahkan perubahan aturan penilaian tanpa mengubah file lain

3. tampilan.py (Class View)


<img width="955" height="504" alt="tampilan" src="https://github.com/user-attachments/assets/8c87d3c6-52d7-4ed4-a946-f0b1d06ce46e" />



File ini berfungsi sebagai class view yang mengatur tampilan output ke pengguna.

Penjelasan:

Class Tampilan bertugas menampilkan data mahasiswa ke layar

Method tampilkan_tabel() digunakan untuk:

Menampilkan nama, NIM, nilai, dan grade

Menyajikan hasil secara rapi dan terstruktur

Tidak mengolah data, hanya menampilkan hasil

Tujuan penggunaan:

Menerapkan konsep separation of concerns

Memisahkan tampilan dari proses

Memudahkan pengubahan tampilan tanpa mengganggu logika program

4. main.py (Program Utama)


<img width="955" height="504" alt="main" src="https://github.com/user-attachments/assets/2ea512d0-75f7-4168-a4d6-48ea2cef27b7" />



File ini merupakan inti program yang menghubungkan seluruh class.

Penjelasan:

Mengambil input dari pengguna:

Nama mahasiswa

NIM

Nilai

Melakukan validasi input menggunakan try-except

Membuat objek:

Mahasiswa (data)

NilaiProcessor (proses)

Tampilan (view)

Menjalankan alur program dari awal hingga akhir

Tujuan penggunaan:

Mengatur alur program secara keseluruhan

Menjadi penghubung antara data, proses, dan tampilan

Menghindari penulisan kode yang bercampur dalam satu file

## Output Program


<img width="955" height="504" alt="output" src="https://github.com/user-attachments/assets/18ed7562-bca0-4b04-867c-7c1403ed2a93" />

