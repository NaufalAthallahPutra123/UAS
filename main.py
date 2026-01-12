from mahasiswa import Mahasiswa
from proses import NilaiProcessor
from tampilan import Tampilan

try:
    nama = input("Masukkan Nama Mahasiswa : ")
    nim = input("Masukkan NIM            : ")
    nilai = int(input("Masukkan Nilai (0-100)  : "))

    if nilai < 0 or nilai > 100:
        raise ValueError("Nilai harus antara 0 - 100")

    mhs = Mahasiswa(nama, nim, nilai)
    proses = NilaiProcessor()
    view = Tampilan()

    grade = proses.tentukan_grade(mhs.nilai)
    view.tampilkan_tabel(mhs, grade)

except ValueError as e:
    print("Error:", e)
