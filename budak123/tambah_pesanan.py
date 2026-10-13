import csv
import os
from models import PesananJoki

def simpan_pesanan():
    print("\n=== TAMBAH PESANAN JOKI ===")
    nama_klien = input("Nama Klien   : ").strip()
    jenis_joki = input("Jenis Joki   : ").strip()
    harga = input("Harga (Rp)   : ").strip()

    if not nama_klien or not jenis_joki or not harga:
        print("\n[PERINGATAN] Semua kolom harus diisi!\n")
        return

    pesanan = PesananJoki(nama_klien, jenis_joki, harga)

    file_exists = os.path.exists("pesanan.csv")

    with open("pesanan.csv", "a", newline="", encoding="utf-8") as file:
        writer = csv.writer(file)
        if not file_exists:
            writer.writerow(["Nama Klien", "Jenis Joki", "Harga", "Status"])
        writer.writerow(pesanan.to_list())

    print("\n[BERHASIL] Pesanan joki berhasil ditambahkan.\n")

def main():
    while True:
        print("=== MENU TAMBAH PESANAN ===")
        print("1. Tambah Pesanan")
        print("0. Keluar")
        pilihan = input("Pilih menu: ")

        if pilihan == "1":
            simpan_pesanan()
        elif pilihan == "0":
            print("Program selesai.")
            break
        else:
            print("Pilihan tidak valid.\n")

if __name__ == "__main__":
    main()