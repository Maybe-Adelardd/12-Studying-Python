# Soal Praktikum 4 Python: Error Finding - Penulisan Tipe Data

# Perhatikan kode berikut. Tugas Anda:
# 1. Temukan dan jelaskan semua kesalahan yang menyebabkan program gagal dijalankan atau menghasilkan output yang tidak sesuai.
# 2. Perbaiki kode tersebut hingga dapat berjalan dengan benar dan menghasilkan output yang logis.

nama = "Dimas Setiawan" #Tambahkan string atau quote di sebelum dan sesudah Dimas Setiawan.
umur = 21 #Hapus string pada angka 21 karena termasuk integer.
berat = 65.4 #Hapus string pada angka 65.4 karena termasuk float/double.
tinggi = 170
bmi = berat / ((tinggi / 100) ** 2)
status_siswa = True #Hapus string pada True karena termasuk bool.

"""

BMI adalah singkatan dari Indeks Massa Tubuh (Body Mass Index).
BMI adalah ukuran yang digunakan untuk menentukan
apakah berat badan seseorang ideal, kurang, atau berlebih
berdasarkan tinggi badan mereka. Perhitungan BMI dilakukan dengan membagi berat badan (dalam kilogram) dengan kuadrat tinggi badan (dalam meter).

"""

print("Nama:", nama)
print("Umur:", umur, "tahun")
print("Berat badan:", berat, "kg")
print("BMI:", round (bmi, 2))
print("Siswa Aktif:", bool (status_siswa))