# Contoh Materi Kode Python

# 1. Variabel dan Tipe Data
# Variabel adalah tempat penyimpanan untuk data.
# Tipe data: int, float, string, boolean
# Penulisan variabel: nama_variabel = nilai

nama = "John Doe"
umur = 25
tinggi = 175.5
sudah_menikah = False

# 2. Operasi Matematika
# Operasi dasar: +, -, *, /, %
# Operasi tambahan: ** (pangkat), // (pembagian bulat)
# Operasi gabungan: +=, -=, *=, /=

a = 10
b = 5
hasil_penjumlahan = a + b
hasil_pengurangan = a - b
hasil_perkalian = a * b
hasil_pembagian = a / b
hasil_pangkat = a ** b
hasil_pembagian_bulat = a // b
sisa_pembagian = a % b

# 3. Struktur Pemilihan (If-Else)
# Digunakan untuk pengambilan keputusan.
# if kondisi:
#    aksi1
# elif kondisi2:
#    aksi2
# else:
#    aksi_default

nilai = 85
if nilai >= 90:
    grade = "A"
elif nilai >= 80:
    grade = "B"
elif nilai >= 70:
    grade = "C"
else:
    grade = "D"

# 4. Perulangan (Looping)
# Digunakan untuk mengeksekusi blok kode secara berulang.
# Ada dua jenis loop utama: for dan while.

# Perulangan dengan for
for i in range(5):  # Mengulangi 5 kali
    print("Perulangan ke-", i+1)

# Perulangan dengan while
jumlah = 0
while jumlah < 5:
    print("Jumlah:", jumlah)
    jumlah += 1

# 5. Fungsi
# Blok kode yang dapat digunakan kembali.
# Definisi fungsi: def nama_fungsi(parameter):
#                    aksi

def tambah(a, b):
    return a + b

def kali(a, b):
    return a * b

# Penggunaan fungsi
hasil_tambah = tambah(3, 4)
hasil_kali = kali(2, 5)

print("Hasil penjumlahan:", hasil_tambah)
print("Hasil perkalian:", hasil_kali)
