from collections import deque

# ==========================================
# 1. LIST - Penyimpanan data secara berurutan
# ==========================================

data_mahasiswa = [
    "Ardit",
    "Bela",
    "Cici",
    "Danu"
]

print("=== DATA MAHASISWA ===")

for mahasiswa in data_mahasiswa:
    print(mahasiswa)


# ==========================================
# 2. STACK - Fitur Undo
# ==========================================

undo_stack = []

print("\n=== FITUR UNDO ===")

# Menambahkan aktivitas ke Stack
undo_stack.append("Menambahkan data Ardit")
undo_stack.append("Menambahkan data Bela")
undo_stack.append("Menambahkan data Cici")

print("Aktivitas sebelum Undo:")
print(undo_stack)

# Mengambil aktivitas terakhir
aktivitas_terakhir = undo_stack.pop()

print("Aktivitas yang dibatalkan:")
print(aktivitas_terakhir)

print("Aktivitas setelah Undo:")
print(undo_stack)


# ==========================================
# 3. QUEUE - Sistem antrean
# ==========================================

antrian = deque()

print("\n=== SISTEM ANTREAN ===")

# Menambahkan data ke antrean
antrian.append("Mahasiswa Ardit")
antrian.append("Mahasiswa Bela")
antrian.append("Mahasiswa Cici")

print("Antrean:")
print(antrian)

# Mengambil data paling depan
diproses = antrian.popleft()

print("Data yang diproses:")
print(diproses)

print("Antrean setelah diproses:")
print(antrian)


# ==========================================
# 4. DICTIONARY - Pencarian berdasarkan key
# ==========================================

mahasiswa = {
    "2301001": "Ardit",
    "2301002": "Bela",
    "2301003": "Cici",
    "2301004": "Danu"
}

print("\n=== PENCARIAN BERDASARKAN KEY ===")

nim = "2301003"

if nim in mahasiswa:
    print("Mahasiswa dengan NIM", nim, "adalah", mahasiswa[nim])
else:
    print("Data mahasiswa tidak ditemukan")