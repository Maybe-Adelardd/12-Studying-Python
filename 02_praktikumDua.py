#Soal 2: Konversi Tipe Data

#Tugas:
# Lakukan konversi tipe data berikut:
# • Konversi usia ke string
# • Konversi tinggi_badan ke integer
# • Konversi mahasiswa_aktif ke integer
# Tampilkan hasil konversi dan tipe datanya.

namaLengkap = "Adelard Tyan Munandar"
usia = 16
tinggiBadan = 172.5
mahasiswaAktif = False

usiaStr = str(usia)
tinggiBadanInt = int(tinggiBadan)
mahasiswaAktifInt = int(mahasiswaAktif)

print("Usia: ", usiaStr, "& Tipe Data:", type(usiaStr))
print("Tinggi Badan: ", tinggiBadanInt, "& Tipe Data:", type(tinggiBadanInt))
print("Status sebagai Mahasiswa: ", mahasiswaAktifInt, "& Tipe Data:", type(mahasiswaAktifInt))

