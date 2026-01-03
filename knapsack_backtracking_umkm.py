# ==================================================
# 0/1 Knapsack Problem - Dynamic Programming
# Studi Kasus: Produk Kecantikan UMKM
# ==================================================

# Data produk (Nama, Berat, Keuntungan)
produk = [
    ("Facial Wash", 5, 40),
    ("Toner Wajah", 6, 45),
    ("Serum", 4, 60),
    ("Moisturizer", 7, 70),
    ("Sunscreen", 6, 65),
    ("Sheet Mask", 3, 30),
    ("Night Cream", 8, 75),
    ("Essence", 9, 55),
    ("Lip Cream", 2, 35),
    ("Micellar Water", 10, 50)
]

kapasitas = 50
jumlah_item = len(produk)

# =======================
# Menampilkan Data Produk
# =======================
print("=== DATA PRODUK KECANTIKAN UMKM ===")
print(f"{'No':<4} {'Nama Produk':<20} {'Berat (kg)':<12} {'Keuntungan':<12}")
print("-" * 55)

for i, (nama, berat, keuntungan) in enumerate(produk, start=1):
    print(f"{i:<4} {nama:<20} {berat:<12} {keuntungan:<12}")

print("\nKapasitas Gudang:", kapasitas, "kg")

# =======================
# Proses Dynamic Programming
# =======================
dp = [[0] * (kapasitas + 1) for _ in range(jumlah_item + 1)]

for i in range(1, jumlah_item + 1):
    nama, berat, keuntungan = produk[i - 1]
    for w in range(kapasitas + 1):
        if berat <= w:
            dp[i][w] = max(
                dp[i - 1][w],
                dp[i - 1][w - berat] + keuntungan
            )
        else:
            dp[i][w] = dp[i - 1][w]

# =======================
# Penelusuran Item Terpilih
# =======================
w = kapasitas
total_berat = 0
item_terpilih = []

print("\n=== PROSES PENELUSURAN ITEM TERPILIH ===")
print(f"{'Produk':<20} {'Status':<10} {'Berat (kg)':<10} {'Keuntungan':<12}")
print("-" * 55)

w = kapasitas
total_berat = 0
item_terpilih = []

for i in range(jumlah_item, 0, -1):
    nama, berat, keuntungan = produk[i - 1]

    if dp[i][w] != dp[i - 1][w]:
        print(f"{nama:<20} {'DIPILIH':<10} {berat:<10} {keuntungan:<12}")
        item_terpilih.append(nama)
        total_berat += berat
        w -= berat
    else:
        print(f"{nama:<20} {'TIDAK':<10} {'-':<10} {'-':<12}")

item_terpilih.reverse()

# =======================
# Hasil Akhir
# =======================
print("\n=== HASIL AKHIR ===")
print("Keuntungan Maksimum :", dp[jumlah_item][kapasitas])
print("Total Berat :", total_berat, "kg")
print("Produk Terpilih :")
for item in item_terpilih:
    print("-", item)
