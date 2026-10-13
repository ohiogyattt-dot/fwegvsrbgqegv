import csv
import os
from models import RatingHotel

def simpan_rating():
    print("\n=== TAMBAH RATING HOTEL ===")
    nama_hotel = input("Nama Hotel    : ").strip()
    kota = input("Kota          : ").strip()
    rating = input("Rating (1-5)  : ").strip()
    jumlah_ulasan = input("Jumlah Ulasan : ").strip()

    if not nama_hotel or not kota or not rating or not jumlah_ulasan:
        print("\n[PERINGATAN] Semua kolom harus diisi!\n")
        return

    hotel_rating = RatingHotel(nama_hotel, kota, rating, jumlah_ulasan)

    file_exists = os.path.exists("hotel_rating.csv")

    with open("hotel_rating.csv", "a", newline="", encoding="utf-8") as file:
        writer = csv.writer(file)
        if not file_exists:
            writer.writerow(["Nama Hotel", "Kota", "Rating (1-5)", "Jumlah Ulasan", "Kategori"])
        writer.writerow(hotel_rating.to_list())

    print("\n[BERHASIL] Rating hotel berhasil ditambahkan.\n")

def main():
    while True:
        print("=== MENU TAMBAH RATING ===")
        print("1. Tambah Rating")
        print("0. Keluar")
        pilihan = input("Pilih menu: ")

        if pilihan == "1":
            simpan_rating()
        elif pilihan == "0":
            print("Program selesai.")
            break
        else:
            print("Pilihan tidak valid.\n")

if __name__ == "__main__":
    main()