# ==========================================
# PROGRAM CATATAN KEUANGAN BULANAN
# DENGAN KATEGORI & EVALUASI KEUANGAN
# ==========================================

# Menyimpan semua transaksi
transaksi = []

# Menyimpan total pemasukan
total_pemasukan = 0


# Menampilkan menu utama
def tampilkan_menu():
    print("\n=== CATATAN KEUANGAN BULANAN ===")
    print("1. Tambah Pemasukan")
    print("2. Tambah Pengeluaran")
    print("3. Tampilkan Semua Transaksi")
    print("4. Evaluasi Keuangan Bulanan")
    print("5. Keluar")
    print("================================")


# Menambahkan pemasukan
def tambah_pemasukan():
    global total_pemasukan
    nominal = int(input("Masukkan jumlah pemasukan: "))
    total_pemasukan += nominal
    print("Pemasukan berhasil ditambahkan.")


# Menambahkan pengeluaran dengan kategori
def tambah_pengeluaran():
    print("\nKategori Pengeluaran:")
    print("1. Primer")
    print("2. Sekunder")
    print("3. Tersier")

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
    print("Pengeluaran berhasil ditambahkan.")


# Menampilkan semua transaksi
def tampilkan_transaksi():
    if len(transaksi) == 0:
        print("Belum ada transaksi.")
        return
    print("\n=== RINCIAN TRANSAKSI ===")
    print("\n" + "-" * 70)
    print(f"{'NO':^4} | {'KATEGORI':^10} | {'KETERANGAN':^30} | {'NOMINAL':^15}")
    print("-" * 70)

    total_pengeluaran = 0  # penampung total

    for i in range(len(transaksi)):
        data = transaksi[i]

        kategori = data['kategori']
        keterangan = data['keterangan']
        nominal = data['nominal']

        if len(keterangan) > 30:
            keterangan = keterangan[:27] + "..."

        print(
            f"{i+1:^4} | "
            f"{kategori:<10} | "
            f"{keterangan:<30} | "
            f"Rp {nominal:>12,}"
        )

        total_pengeluaran += nominal  # akumulasi total

    print("-" * 70)
    print(
        f"{'TOTAL':<3} | "
        f"{'':<10} | "
        f"{'TOTAL PENGELUARAN':<30} | "
        f"Rp {total_pengeluaran:>12,}"
    )
    print("-" * 70)


# Evaluasi keuangan bulanan berdasarkan konsep 50-30-20
def evaluasi_keuangan():
    total_pengeluaran = 0
    primer = 0
    sekunder = 0
    tersier = 0

    # Menghitung total pengeluaran per kategori
    for data in transaksi:
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

    print("\n=== EVALUASI KEUANGAN ===")

    if total_pemasukan == 0:
        print("Belum ada pemasukan yang tercatat.")
        return

    persen_primer = (primer / total_pemasukan) * 100
    persen_sekunder = (sekunder / total_pemasukan) * 100
    persen_tersier = (tersier / total_pemasukan) * 100

    kondisi_baik = True

    # Kondisi paling berat
    if total_pengeluaran > total_pemasukan:
        print(
            "Total pengeluaran Anda melebihi pemasukan.\n"
            "Disarankan untuk mengevaluasi kembali pola pengeluaran agar keuangan lebih stabil. 😊"
        )
        kondisi_baik = False

    # Evaluasi kategori
    if persen_sekunder > 50:
        print(
            "Pengeluaran untuk kebutuhan sekunder melebihi 50% dari total pemasukan.\n"
            "Sebaiknya kurangi pengeluaran non-primer di bulan berikutnya."
        )
        kondisi_baik = False

    if persen_tersier > 25:
        print(
            "Pengeluaran untuk kebutuhan tersier tergolong tinggi.\n"
            "Pertimbangkan untuk membatasi pengeluaran bersifat keinginan. "
        )
        kondisi_baik = False

    # Kondisi sehat
    if kondisi_baik:
        print(
            "Pengelolaan keuangan Anda pada bulan ini tergolong baik.\n"
            "Pola pengeluaran sudah cukup seimbang, pertahankan kebiasaan ini. 😎👍"
        )


# Program utama
def main():
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
            print(
                "Terima kasih telah menggunakan program catatan keuangan kami.\n"
                "Semoga pengelolaan keuangan Anda menjadi lebih baik di bulan berikutnya. 😊🙏"
            )
            break
        else:
            print("Pilihan tidak valid.")


# Menjalankan program
main()