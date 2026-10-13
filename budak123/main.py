import subprocess

def buka_tambah_rating():
    subprocess.run(["python", "tambah_rating.py"])

def buka_tampil_rating():
    subprocess.run(["python", "tampil_rating.py"])

def menu_utama():
    while True:
        print("\n" + "=" * 40)
        print(" SISTEM RATING HOTEL ".center(40, "="))
        print("=" * 40)
        print("1. Tambah Rating Hotel")
        print("2. Tampilkan Daftar Rating Hotel")
        print("0. Keluar")
        print("=" * 40)
        pilihan = input("Pilih menu: ")
        
        if pilihan == "1":
            buka_tambah_rating()
        elif pilihan == "2":
            buka_tampil_rating()
        elif pilihan == "0":
            print("Terima kasih.")
            break
        else:
            print("Pilihan tidak valid!")

if __name__ == "__main__":
    menu_utama()