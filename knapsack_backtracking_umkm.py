# Data produk kecantikan UMKM
weights = [5, 6, 4, 7, 6, 3, 8, 9, 2, 10]      # berat (kg)
profits = [40, 45, 60, 70, 65, 30, 75, 55, 35, 50]  # keuntungan
capacity = 50
n = len(weights)

# Membuat tabel DP
dp = [[0 for _ in range(capacity + 1)] for _ in range(n + 1)]

# Proses Dynamic Programming
for i in range(1, n + 1):
    for w in range(capacity + 1):
        if weights[i - 1] <= w:
            dp[i][w] = max(
                dp[i - 1][w],
                dp[i - 1][w - weights[i - 1]] + profits[i - 1]
            )
        else:
            dp[i][w] = dp[i - 1][w]

# Menentukan item yang terpilih
w = capacity
selected_items = []

for i in range(n, 0, -1):
    if dp[i][w] != dp[i - 1][w]:
        selected_items.append(i)
        w -= weights[i - 1]

selected_items.reverse()

# Menampilkan hasil
print("Nilai maksimum keuntungan:", dp[n][capacity])
print("Item terpilih:", selected_items)
print("Total berat:", sum(weights[i - 1] for i in selected_items))
