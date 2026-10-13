import subprocess

def buka_tambah_pesanan():
    subprocess.run(["python", "tambah_pesanan.py"])

def buka_tampil_pesanan():
    subprocess.run(["python", "tampil_pesanan.py"])

def menu_utama():
    while True:
        print("\n" + "=" * 40)
        print(" SISTEM JASA JOKI ".center(40, "="))
        print("=" * 40)
        print("1. Tambah Pesanan Joki")
        print("2. Tampilkan Pesanan Joki")
        print("0. Keluar")
        print("=" * 40)
        pilihan = input("Pilih menu: ")
        
        if pilihan == "1":
            buka_tambah_pesanan()
        elif pilihan == "2":
            buka_tampil_pesanan()
        elif pilihan == "0":
            print("Terima kasih.")
            break
        else:
            print("Pilihan tidak valid!")

if __name__ == "__main__":
    menu_utama()