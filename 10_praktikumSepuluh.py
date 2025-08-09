# Soal Praktikum 10 Python: Penulisan Operator

# Tuliskan dan jalankan kode Python sesuai perintah yang diberikan pada setiap soal. Amati hasilnya.
# Soal 10: Gabungan Operator (Aritmatika + Logika)

# Tugas:
# Diberikan variabel:
# nilai_matematika = 80
# nilai_fisika = 70
# rata_rata = (nilai_matematika + nilai_fisika) / 2
# Buat ekspresi logika yang menghasilkan True jika:
# Rata-rata minimal 75 dan
# Nilai matematika lebih besar dari nilai fisika
# Cetak hasil evaluasi ekspresi tersebut.

nilaiMatematika = 80
nilaiFisika = 70
rataRata = (nilaiMatematika + nilaiFisika) / 2

if rataRata >= 75 and nilaiMatematika > nilaiFisika:
    print(True)
else:
    print(False)
