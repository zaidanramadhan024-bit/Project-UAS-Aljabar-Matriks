import zaidan054

mat_A = [
    [10, 20, 30],
    [40, 50, 60]
]

mat_B = [
    [5, 5, 5],
    [5, 5, 5]
]

# Menjalankan fungsi penjumlahan
hasil_tambah = zaidan054.tambah_matriks(mat_A, mat_B)
print("Hasil Penjumlahan Matriks:")
for baris in hasil_tambah:
    print(baris)

# Menjalankan fungsi pengurangan
hasil_kurang = zaidan054.kurang_matriks(mat_A, mat_B)
print("Hasil Pengurangan Matriks:")
for baris in hasil_kurang:
    print(baris)