# Soal Praktikum 12 Python: Aritmatika

# Buatlah program Python untuk menyelesaikan permasalahan berikut:

# Seorang pedagang menjual tiga jenis barang dengan rincian sebagai berikut:
# Barang A: Harga satuan Rp12.500
# Barang B: Harga satuan Rp7.300
# Barang C: Harga satuan Rp2.850

# Ketentuan pembelian:
# Jika total pembelian lebih dari Rp150.000, pelanggan mendapat diskon 15%
# Jika total pembelian lebih dari Rp100.000 tapi kurang dari atau sama dengan Rp150.000, pelanggan mendapat diskon 10%
# Jika total pembelian kurang dari atau sama dengan Rp100.000, tidak ada diskon

# Tugas Anda:
# 1. Minta input jumlah pembelian untuk masing-masing barang.
# 2. Hitung total harga kotor (sebelum diskon)
# 3. Hitung jumlah diskon yang diperoleh pelanggan
# 4. Hitung total harga bersih (setelah diskon)
# 5. Tampilkan semua hasil perhitungan dengan format yang rapi

barangA = 12500
barangB = 7300
barangC = 2850

jumlahPembelianBarangA = int(input("Masukkan jumlah barang A: "))
jumlahPembelianBarangB = int(input("Masukkan jumlah barang B: "))
jumlahPembelianBarangC = int(input("Masukkan jumlah barang C: "))

totalHargaKotor = (jumlahPembelianBarangA * barangA) + (jumlahPembelianBarangB * barangB) + (jumlahPembelianBarangC * barangC)
print("Harga Kotor: Rp.", totalHargaKotor)

if totalHargaKotor > 150000:
    diskon1 = totalHargaKotor * 0.15
    hargaFinal1 = totalHargaKotor - diskon1 
    print("Diskon yang diperoleh: Rp.", diskon1)
    print("Harga Final: Rp.", hargaFinal1)

elif totalHargaKotor > 100000 and totalHargaKotor <= 150000:
    diskon2 = totalHargaKotor * 0.10
    hargaFinal2 = totalHargaKotor - diskon2
    print("Diskon yang diperoleh: Rp.", diskon2)
    print("Harga Final: Rp.", hargaFinal2)

else:
    diskon3 = totalHargaKotor * 0.0
    hargaFinal3 = totalHargaKotor - diskon3
    print("Diskon yang diperoleh: Rp.", diskon3)
    print("Harga Final: Rp.", hargaFinal3)
