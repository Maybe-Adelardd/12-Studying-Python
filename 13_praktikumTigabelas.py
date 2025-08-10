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

def inputNilai (mataPelajaran):
    while True:
        try:
            nilai = int(input(f"Masukkan nilai {mataPelajaran} (0-100): "))
            if 0 <= nilai <= 100:
                return nilai
            else:
                print("Nilai harus antara 0 sampai 100. Silakan coba lagi.")
        except ValueError:
            print("Input tidak valid. Masukkan angka bulat.")

matematika = inputNilai("Matematika")
bahasaIndonesia = inputNilai("Bahasa Indonesia")
ipa = inputNilai("IPA")

rataRata = (matematika + bahasaIndonesia + ipa) / 3

nilaiBawah70 = 0
if matematika < 70:
    nilaiBawah70 += 1
if bahasaIndonesia < 70:
    nilaiBawah70 += 1
if ipa < 70:
    nilaiBawah70 += 1
    
nilaiIstimewa = matematika > 85 and bahasaIndonesia > 85 and ipa > 85

if nilaiIstimewa:
    status = "Lulus dengan Predikat Istimewa"
elif nilaiBawah70 >= 2:
    status = "Tidak Lulus"
elif nilaiBawah70 == 1:
    if (matematika > 80 and bahasaIndonesia > 80) or  (matematika > 80 and ipa > 80) or  (bahasaIndonesia > 80 and ipa > 80):
        status = "Lulus Bersyarat"
    else:
        status = "Tidak Lulus"
elif matematika >= 70 and bahasaIndonesia >= 70 and ipa >= 70 and rataRata >= 75:
    status = "Lulus"
else:
    status = "Tidak Lulus"

print("Status Kelulusan:", status)