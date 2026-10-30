PANDUAN PROJECT SPK PEMILIHAN LAPTOP
METODE MOORA

==================================================
1. DESKRIPSI PROJECT
==================================================

Project ini merupakan aplikasi Sistem Pendukung
Keputusan (SPK) untuk membantu pemilihan laptop
menggunakan metode MOORA (Multi-Objective
Optimization on the basis of Ratio Analysis).

Aplikasi dibuat menggunakan Python dan Streamlit.

Fitur aplikasi:
- Menampilkan data alternatif laptop.
- Menampilkan kriteria dan bobot.
- Melakukan normalisasi matriks keputusan.
- Menghitung nilai optimasi MOORA.
- Menampilkan hasil perangkingan laptop.

==================================================
2. STRUKTUR FOLDER
==================================================

Pastikan folder project memiliki susunan berikut:

C:\SPK_Moora
|
|-- .venv
|-- app.py
|-- requirements.txt
|-- README.txt

Keterangan:
- .venv           : lingkungan Python virtual.
- app.py          : kode utama aplikasi.
- requirements.txt: daftar library yang diperlukan.
- README.txt      : panduan penggunaan project.

==================================================
3. PERSIAPAN PROJECT
==================================================

Pastikan Python sudah terinstal di komputer.

Buka PowerShell, kemudian masuk ke folder project
dengan perintah:

cd C:\SPK_Moora

Buat virtual environment dengan perintah:

py -m venv .venv

Aktifkan virtual environment:

.\.venv\Scripts\Activate.ps1

Jika muncul pesan bahwa eksekusi script diblokir,
jalankan perintah berikut:

Set-ExecutionPolicy -Scope Process -ExecutionPolicy Bypass

Kemudian aktifkan kembali:

.\.venv\Scripts\Activate.ps1

Jika berhasil, prompt akan menampilkan:

(.venv) PS C:\SPK_Moora>

Catatan:
Tulisan prompt di atas tidak perlu diketik ulang.

==================================================
4. INSTALASI LIBRARY
==================================================

Pastikan file requirements.txt sudah tersedia dan
berisi daftar library yang diperlukan.

Jalankan perintah:

python -m pip install -r requirements.txt

Library utama yang digunakan:
- Streamlit
- Pandas
- NumPy

Tunggu hingga proses instalasi selesai.

==================================================
5. MENJALANKAN APLIKASI
==================================================

Pastikan file app.py sudah tersedia dan berisi
kode program aplikasi.

Jalankan aplikasi dengan perintah:

python -m streamlit run app.py

Jika aplikasi berhasil dijalankan, buka browser
dan akses alamat:

http://localhost:8501

Untuk menghentikan aplikasi, tekan:

Ctrl + C

di terminal PowerShell.

==================================================
6. METODE MOORA
==================================================

MOORA digunakan untuk mengevaluasi alternatif
berdasarkan sejumlah kriteria yang memiliki bobot
dan atribut benefit atau cost.

Kriteria penelitian:

C1 Harga                 Bobot 0,20 - Cost
C2 Kapasitas Baterai     Bobot 0,10 - Benefit
C3 RAM                   Bobot 0,20 - Benefit
C4 CPU                   Bobot 0,20 - Benefit
C5 Hardisk               Bobot 0,20 - Benefit
C6 Ukuran                Bobot 0,10 - Cost

Total bobot: 1,00

Normalisasi matriks keputusan:

x*ij = xij / sqrt(sum(xij^2))

Nilai optimasi MOORA:

Yi = jumlah nilai kriteria Benefit
     dikurangi jumlah nilai kriteria Cost

Alternatif dengan nilai Yi tertinggi menjadi
alternatif dengan peringkat terbaik.

==================================================
7. SUMBER PENELITIAN
==================================================

Rusadin, F. A., Tatuhey, E. L., dan Lahallo, J.
(2024).

Sistem Pendukung Keputusan Pemilihan Laptop
Menggunakan Metode MOORA pada Master Komputer.

Progresif: Jurnal Ilmiah Komputer,
Vol. 20, No. 2, halaman 1042-1053.

DOI:
https://doi.org/10.35889/progresif.v20i2.1932

==================================================
8. CATATAN
==================================================

Pastikan file app.py dan requirements.txt tidak
kosong sebelum menjalankan aplikasi.

Jika muncul error, periksa:
- Apakah virtual environment sudah aktif.
- Apakah library sudah berhasil diinstal.
- Apakah nama file sudah benar.
- Apakah terminal berada di folder project.
- Apakah file app.py berisi kode program.

==================================================
AKHIR README
==================================================