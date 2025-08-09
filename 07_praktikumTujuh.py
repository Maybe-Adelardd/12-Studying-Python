# Soal Praktikum 7 Python: Penulisan Operator
# Tuliskan dan jalankan kode Python sesuai perintah yang diberikan pada setiap soal. Amati hasilnya.

# Soal 7: Operator Aritmatika

# Tugas:
# Buat dua variabel:
# x = 15
# y = 4

# Lalu, hitung dan tampilkan hasil dari:
# 1. Penjumlahan
# 2. Pengurangan
# 3. Perkalian
# 4. Pembagian
# 5. Modulus
# 6. Pangkat
# 7. Pembagian bulat (floor division)

x = 15
y = 4

def penjumlahan(x, y):
    hasil = x + y
    print("Penjumlahan: ", hasil)
    return hasil

def pengurangan(x, y):
    hasil = x - y
    print("Pengurangan: ", hasil)
    return hasil

def perkalian(x, y):
    hasil = x * y
    print("Perkalian: ", hasil)
    return hasil

def pembagian(x, y):
    hasil = x / y
    print("Pembagian: ", hasil)
    return hasil

def modulus(x, y):
    hasil = x % y
    print("Modulus: ", hasil)
    return hasil

def pangkat(x, y):
    hasil = x ** y
    print("Pangkat: ", hasil)
    return hasil

def floorDivision(x, y):
    hasil = x // y
    print("Floor Division: ", hasil)
    return hasil

penjumlahan(x, y)
pengurangan(x, y)
perkalian(x, y)
pembagian(x, y)
modulus(x, y)
pangkat(x, y)
floorDivision(x, y)