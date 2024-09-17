# Daftar siswa dengan nilai ujian
siswa = [
    {"nama": "Rina", "nilai": 85},
    {"nama": "Toni", "nilai": 92},
    {"nama": "Siti", "nilai": 78},
    {"nama": "Andi", "nilai": 88},
    {"nama": "Udin", "nilai": 65},
    {"nama": "Asep", "nilai": 90},
    {"nama": "Farhan", "nilai": 84}
]

# Fungsi Merge Sort
def merge_sort_siswa(list_siswa):
    if len(list_siswa) > 1:
        mid = len(list_siswa) // 2
        left_half = list_siswa[:mid]
        right_half = list_siswa[mid:]

        # Rekursif untuk memecah daftar
        merge_sort_siswa(left_half)
        merge_sort_siswa(right_half)

        i = j = k = 0

        # Menggabungkan kembali left_half dan right_half
        while i < len(left_half) and j < len(right_half):
            if left_half[i]['nilai'] > right_half[j]['nilai']:
                list_siswa[k] = left_half[i]
                i += 1
            else:
                list_siswa[k] = right_half[j]
                j += 1
            k += 1

        # Menambahkan elemen yang tersisa
        while i < len(left_half):
            list_siswa[k] = left_half[i]
            i += 1
            k += 1

        while j < len(right_half):
            list_siswa[k] = right_half[j]
            j += 1
            k += 1

# Panggil fungsi Merge Sort
merge_sort_siswa(siswa)

# Menampilkan hasil sorting
print("Daftar Siswa Berdasarkan Nilai (Tertinggi ke Terendah):")
for s in siswa:
    print(f"Nama: {s['nama']}, Nilai: {s['nilai']}")
