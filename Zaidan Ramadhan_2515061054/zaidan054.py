def tambah_matriks(A, B):
    baris = len(A)
    kolom = len(A[0])
    
    # Inisialisasi matriks hasil dengan nilai 0
    hasil = [[0 for _ in range(kolom)] for _ in range(baris)]
    
    for i in range(baris):
        for j in range(kolom):
            # Logika: Penjumlahan elemen pada posisi yang sama
            hasil[i][j] = A[i][j] + B[i][j]
            
    return hasil

def kurang_matriks(A, B):
    baris = len(A)
    kolom = len(A[0])
    
    # Inisialisasi matriks hasil dengan nilai 0
    hasil = [[0 for _ in range(kolom)] for _ in range(baris)]
    
    for i in range(baris):
        for j in range(kolom):
            # Logika: Pengurangan elemen pada posisi yang sama
            hasil[i][j] = A[i][j] - B[i][j]
            
    return hasil