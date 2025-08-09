# Soal Praktikum 13 Python: Operator Perbandingan

# Buatlah sebuah program Python yang dapat menentukan status kelulusan siswa dari tiga mata pelajaran utama: Matematika, Bahasa Indonesia, dan IPA. 
# Setiap nilai berada dalam rentang 0-100.

# Ketentuan kelulusan siswa:
# 1. Nilai minimal setiap mata pelajaran adalah 70.
# 2. Nilai rata-rata ketiga mata pelajaran minimal 75.
# 3. Jika satu mata pelajaran di bawah 70, tetapi dua lainnya di atas 80, siswa dapat lulus bersyarat.
# 4. Jika dua atau lebih mata pelajaran di bawah 70, siswa tidak lulus.
# 5. Jika semua nilai di atas 85, maka siswa lulus dengan predikat istimewa.

# Tugas Anda:
# Minta input nilai ketiga mata pelajaran.
# Gunakan operator perbandingan dan logika untuk menentukan status kelulusan siswa.
# Cetak status akhir siswa: Lulus, Lulus Bersyarat, Tidak Lulus, atau Lulus dengan Predikat Istimewa.

# Fungsi untuk meminta input nilai dengan validasi antara 0 dan 100
def input_nilai(mata_pelajaran):
    while True:
        try:
            nilai = int(input(f"Masukkan nilai {mata_pelajaran} (0-100): "))
            if 0 <= nilai <= 100:
                return nilai
            else:
                print("Nilai harus antara 0 sampai 100. Silakan coba lagi.")
        except ValueError:
            print("Input tidak valid. Masukkan angka bulat.")

# Meminta input nilai dari pengguna dengan validasi
matematika = input_nilai("Matematika")
bahasa_indonesia = input_nilai("Bahasa Indonesia")
ipa = input_nilai("IPA")

# Menghitung rata-rata
rata_rata = (matematika + bahasa_indonesia + ipa) / 3

# Menghitung jumlah nilai yang di bawah 70
jumlah_di_bawah_70 = 0
if matematika < 70:
    jumlah_di_bawah_70 += 1
if bahasa_indonesia < 70:
    jumlah_di_bawah_70 += 1
if ipa < 70:
    jumlah_di_bawah_70 += 1

# Mengecek apakah semua nilai di atas 85
jika_istimewa = matematika > 85 and bahasa_indonesia > 85 and ipa > 85

# Menentukan status kelulusan
if jika_istimewa:
    status = "Lulus dengan Predikat Istimewa"
elif jumlah_di_bawah_70 >= 2:
    status = "Tidak Lulus"
elif jumlah_di_bawah_70 == 1:
    if (matematika > 80 and bahasa_indonesia > 80) or \
       (matematika > 80 and ipa > 80) or \
       (bahasa_indonesia > 80 and ipa > 80):
        status = "Lulus Bersyarat"
    else:
        status = "Tidak Lulus"
elif matematika >= 70 and bahasa_indonesia >= 70 and ipa >= 70 and rata_rata >= 75:
    status = "Lulus"
else:
    status = "Tidak Lulus"

# Menampilkan hasil
print("Status Kelulusan:", status)

