# Soal Praktikum 11 Python: Penulisan Operator

# Tuliskan dan jalankan kode Python sesuai perintah yang diberikan pada setiap soal. Amati hasilnya.
# Soal 11: Soal - Operator Logika & Perbandingan

# Tugas:
# Seorang siswa memiliki data:
# Umur: 17 tahun
# Rerata: 83.2
# Sudah lulus semua praktikum wajib: True
# Buat logika untuk menentukan apakah dia berhak ikut magang, dengan syarat:
# Rerata minimal 83.0 dan umur tidak lebih dari 21 tahun, dan sudah lulus semua praktikum wajib.
# Cetak hasil evaluasi ekspresi tersebut.

umur = 17
rerata = 83.2
lulusMapel = True

if rerata >= 83.0 and umur <= 21 and lulusMapel:
    print("Selamat, Kamu Berhak Ikut Magang!")
else:
    print("Maaf, Anda Tidak Memenuhi Persyaratan")