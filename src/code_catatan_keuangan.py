import csv
import os

# ==========================================
# PROGRAM CATATAN KEUANGAN BULANAN (PRO VERSION)
# ==========================================

NAMA_FILE = 'catatan_keuangan.csv'
transaksi = []
total_pemasukan = 0

# --- FUNGSI DATABASE (CSV) ---
def muat_data():
    global total_pemasukan
    if os.path.exists(NAMA_FILE):
        with open(NAMA_FILE, mode='r', newline='', encoding='utf-8') as file:
            reader = csv.DictReader(file)
            for row in reader:
                # Ubah nominal balik jadi integer
                row['nominal'] = int(row['nominal'])
                transaksi.append(row)
                
                # Hitung ulang total pemasukan dari data yang dimuat
                if row['jenis'] == 'Pemasukan':
                    total_pemasukan += row['nominal']

def simpan_data():
    with open(NAMA_FILE, mode='w', newline='', encoding='utf-8') as file:
        fieldnames = ['jenis', 'kategori', 'keterangan', 'nominal']
        writer = csv.DictWriter(file, fieldnames=fieldnames)
        
        writer.writeheader()
        for data in transaksi:
            writer.writerow(data)

# --- FUNGSI MENU UTAMA ---
def tampilkan_menu():
    print("\n=== CATATAN KEUANGAN BULANAN ===")
    print("1. Tambah Pemasukan")
    print("2. Tambah Pengeluaran")
    print("3. Tampilkan Semua Transaksi")
    print("4. Evaluasi Keuangan Bulanan")
    print("5. Keluar")
    print("================================")

def tambah_pemasukan():
    global total_pemasukan
    nominal = int(input("Masukkan jumlah pemasukan: "))
    total_pemasukan += nominal
    
    # Catat ke list transaksi juga biar masuk CSV
    data = {
        "jenis": "Pemasukan",
        "kategori": "Pendapatan",
        "keterangan": "Pemasukan Bulanan",
        "nominal": nominal
    }
    transaksi.append(data)
    simpan_data() # Langsung simpan ke file!
    print("Pemasukan berhasil ditambahkan & disimpan!")

def tambah_pengeluaran():
    print("\nKategori Pengeluaran:")
    print("1. Primer (Kebutuhan Pokok)")
    print("2. Sekunder (Gaya Hidup/Hiburan)")
    print("3. Tersier (Barang Mewah)")

    pilihan = input("Pilih kategori (1-3): ")

    if pilihan == "1":
        kategori = "Primer"
    elif pilihan == "2":
        kategori = "Sekunder"
    elif pilihan == "3":
        kategori = "Tersier"
    else:
        print("Kategori tidak valid.")
        return

    keterangan = input("Masukkan keterangan pengeluaran: ")
    nominal = int(input("Masukkan jumlah pengeluaran: "))

    data = {
        "jenis": "Pengeluaran",
        "kategori": kategori,
        "keterangan": keterangan,
        "nominal": nominal
    }

    transaksi.append(data)
    simpan_data() # Langsung simpan ke file!
    print("Pengeluaran berhasil ditambahkan & disimpan!")

def tampilkan_transaksi():
    if len(transaksi) == 0:
        print("Belum ada transaksi.")
        return
        
    print("\n=== RINCIAN TRANSAKSI ===")
    print("-" * 80)
    print(f"{'NO':^4} | {'JENIS':^12} | {'KATEGORI':^10} | {'KETERANGAN':^25} | {'NOMINAL':^15}")
    print("-" * 80)

    total_pengeluaran = 0

    for i in range(len(transaksi)):
        data = transaksi[i]
        jenis = data['jenis']
        kategori = data['kategori']
        keterangan = data['keterangan']
        nominal = data['nominal']

        if len(keterangan) > 25:
            keterangan = keterangan[:22] + "..."

        print(
            f"{i+1:^4} | "
            f"{jenis:<12} | "
            f"{kategori:<10} | "
            f"{keterangan:<25} | "
            f"Rp {nominal:>12,}"
        )

        if jenis == "Pengeluaran":
            total_pengeluaran += nominal

    print("-" * 80)
    print(f"{'TOTAL PENGELUARAN':<60} | Rp {total_pengeluaran:>12,}")
    print("-" * 80)

def evaluasi_keuangan():
    total_pengeluaran = 0
    primer = 0
    sekunder = 0
    tersier = 0

    for data in transaksi:
        if data["jenis"] == "Pengeluaran":
            total_pengeluaran += data["nominal"]
            if data["kategori"] == "Primer":
                primer += data["nominal"]
            elif data["kategori"] == "Sekunder":
                sekunder += data["nominal"]
            elif data["kategori"] == "Tersier":
                tersier += data["nominal"]

    print("\n=== RINGKASAN KEUANGAN ===")
    print(f"Total Pemasukan   : Rp {total_pemasukan:,}")
    print(f"Total Pengeluaran : Rp {total_pengeluaran:,}")
    print(f"Sisa Saldo        : Rp {total_pemasukan - total_pengeluaran:,}")
    print("================================")

    if total_pemasukan == 0:
        print("\nBelum ada pemasukan yang tercatat. Tidak bisa evaluasi.")
        return

    print("\n=== EVALUASI KEUANGAN ===")
    persen_sekunder = (sekunder / total_pemasukan) * 100
    persen_tersier = (tersier / total_pemasukan) * 100
    kondisi_baik = True

    if total_pengeluaran > total_pemasukan:
        print("- 🚨 BAHAYA: Total pengeluaran melebihi pemasukan (Besar pasak daripada tiang).")
        kondisi_baik = False

    if persen_sekunder > 30: # Standar teori 50/30/20 (Sekunder max 30%)
        print("- ⚠️ PERINGATAN: Pengeluaran sekunder/keinginan lebih dari 30%. Kurangi nongkrong/belanja.")
        kondisi_baik = False

    if persen_tersier > 20: # Standar teori 50/30/20 (Tabungan/Investasi harusnya 20%, jadi tersier jgn gede2)
        print("- ⚠️ PERINGATAN: Pengeluaran tersier terlalu tinggi. Batasi barang mewah!")
        kondisi_baik = False

    if kondisi_baik:
        print("✅ MANTAP: Pengelolaan keuangan bulan ini sangat sehat. Pertahankan! 😎👍")

def main():
    muat_data() # Load data dari CSV pas program jalan
    
    while True:
        tampilkan_menu()
        pilihan = input("Pilih menu (1-5): ")

        if pilihan == "1":
            tambah_pemasukan()
        elif pilihan == "2":
            tambah_pengeluaran()
        elif pilihan == "3":
            tampilkan_transaksi()
        elif pilihan == "4":
            evaluasi_keuangan()
        elif pilihan == "5":
            print("Terima kasih! Data sudah aman tersimpan di 'catatan_keuangan.csv'. 🙏")
            break
        else:
            print("Pilihan tidak valid.")

if __name__ == "__main__":
    main()