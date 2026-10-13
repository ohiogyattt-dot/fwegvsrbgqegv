import csv
import os
from models import RatingHotel

def muat_data():
    daftar_rating = []
    if not os.path.exists("hotel_rating.csv"):
        print("File hotel_rating.csv tidak ditemukan.")
        return daftar_rating

    with open("hotel_rating.csv", newline="", encoding="utf-8") as file:
        reader = csv.reader(file)
        next(reader, None)  # Lewati header
        for row in reader:
            hotel_rating = RatingHotel(
                nama_hotel=row[0],
                kota=row[1],
                rating=row[2],
                jumlah_ulasan=row[3],
                kategori=row[4]
            )
            daftar_rating.append(hotel_rating)
    return daftar_rating

def tampilkan_rating():
    daftar_rating = muat_data()
    if not daftar_rating:
        print("Tidak ada data rating hotel.")
        return

    print("\n=== DAFTAR RATING HOTEL ===\n")
    print(f"{'Nama Hotel':25}{'Kota':15}{'Rating':10}{'Ulasan':15}{'Kategori'}")
    print("-" * 75)
    for hr in daftar_rating:
        print(
            f"{hr.nama_hotel:25}"
            f"{hr.kota:15}"
            f"{hr.rating:10}"
            f"{hr.jumlah_ulasan:15}"
            f"{hr.kategori}"
        )
    print("-" * 75)
    print(f"Total Hotel Terdaftar: {len(daftar_rating)}")

def main():
    while True:
        print("\n=== MENU ===")
        print("1. Tampilkan Rating")
        print("2. Refresh Data")
        print("0. Keluar")
        pilihan = input("Pilih: ")

        if pilihan == "1":
            tampilkan_rating()
        elif pilihan == "2":
            print("Data dimuat ulang...")
            tampilkan_rating()
        elif pilihan == "0":
            print("Program selesai.")
            break
        else:
            print("Pilihan tidak valid.")

if __name__ == "__main__":
    main()