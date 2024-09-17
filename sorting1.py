# Daftar produk
produk = [
    {"nama": "Processor", "harga": 1200000},
    {"nama": "Motherboard", "harga": 1300000},
    {"nama": "RAM", "harga": 500000},
    {"nama": "GPU", "harga": 4500000},
    {"nama": "PSU", "harga": 650000},
    {"nama": "Keyboard", "harga": 500000},
    {"nama": "Monitor", "harga": 3000000},
    {"nama": "Mouse", "harga": 200000}
]

# Fungsi Quicksort
def quicksort_product(product_list):
    if len(product_list) <= 1:
        return product_list
    else:
        pivot = product_list[0]  # Memilih elemen pivot
        less_than = [x for x in product_list[1:] if x['harga'] <= pivot['harga']]
        more_than = [x for x in product_list[1:] if x['harga'] > pivot['harga']]
        return quicksort_product(less_than) + [pivot] + quicksort_product(more_than)

# Panggil fungsi Quicksort
produk_sorted = quicksort_product(produk)

# Menampilkan hasil sorting
print("Daftar Produk Berdasarkan Harga (Murah ke Mahal):")
for p in produk_sorted:
    print(f"Nama: {p['nama']}, Harga: {p['harga']}")
