import csv
import os
from models import PesananJoki

def muat_data():
    daftar_pesanan = []
    if not os.path.exists("pesanan.csv"):
        print("File pesanan.csv tidak ditemukan.")
        return daftar_pesanan

    with open("pesanan.csv", newline="", encoding="utf-8") as file:
        reader = csv.reader(file)
        next(reader, None)  # Lewati header
        for row in reader:
            pesanan = PesananJoki(
                nama_klien=row[0],
                jenis_joki=row[1],
                harga=row[2],
                status=row[3]
            )
            daftar_pesanan.append(pesanan)
    return daftar_pesanan

def tampilkan_pesanan():
    daftar_pesanan = muat_data()
    if not daftar_pesanan:
        print("Tidak ada data pesanan.")
        return

    print("\n=== DAFTAR PESANAN JOKI ===\n")
    print(f"{'Nama Klien':20}{'Jenis Joki':25}{'Harga (Rp)':15}{'Status'}")
    print("-" * 70)
    for pesanan in daftar_pesanan:
        print(
            f"{pesanan.nama_klien:20}"
            f"{pesanan.jenis_joki:25}"
            f"{pesanan.harga:15}"
            f"{pesanan.status}"
        )
    print("-" * 70)
    print(f"Total Pesanan: {len(daftar_pesanan)}")

def main():
    while True:
        print("\n=== MENU ===")
        print("1. Tampilkan Pesanan")
        print("2. Refresh Data")
        print("0. Keluar")
        pilihan = input("Pilih: ")

        if pilihan == "1":
            tampilkan_pesanan()
        elif pilihan == "2":
            print("Data dimuat ulang...")
            tampilkan_pesanan()
        elif pilihan == "0":
            print("Program selesai.")
            break
        else:
            print("Pilihan tidak valid.")

if __name__ == "__main__":
    main()