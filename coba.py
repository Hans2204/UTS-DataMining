import numpy as np
import pandas as pd

# Fungsi untuk menghitung Euclidean distance
def euclidean_distance(x, y):
    return np.sqrt(np.sum((x - y) ** 2))

# Fungsi untuk menghitung Manhattan distance
def manhattan_distance(x, y):
    return np.sum(np.abs(x - y))

# Data dari tabel
dataawal = pd.read_csv('dissimilarity.csv')
data = dataawal.values

# Konversi data keaktifan ke dalam bentuk angka

# Hitung jumlah data dan atribut
num_data = len(data)
num_attributes = len(data[0])

# Matriks dissimilarity campuran
dissimilarity_matrix = np.zeros((num_data, num_data))

# Hitung jarak untuk setiap pasangan data
for i in range(num_data):
    for j in range(num_data):
        dissimilarity = 0
        for k in range(1, num_attributes):  # Mulai dari indeks 1 untuk mengabaikan atribut nominal
            if k == 1:
                dissimilarity += euclidean_distance(data[i][k], data[j][k])
            elif k == 2:
                dissimilarity += manhattan_distance(data[i][k], data[j][k])
            else:
                dissimilarity += 1 if data[i][k] != data[j][k] else 0
        dissimilarity_matrix[i][j] = dissimilarity

# Tampilkan matriks dissimilarity
print("Matriks Dissimilarity Campuran:")
print(dissimilarity_matrix)

# Bagus Kurniawan (Excel)
# Firsta Rahmania Sucahyo (Phyton)
# M. Iqbal Raihan (Phyton + Excel)