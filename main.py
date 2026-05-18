from pabrik_kerajinan import PabrikKerajinan


def tampilkan_demo():
    pabrik = PabrikKerajinan("Pabrik Batagor Kayu & Kaca")
    print(pabrik.memproduksi())
    print()
    print(pabrik.operasi_teknis())
    print()
    print("Catatan penting:")
    print(pabrik._cerita_brand())
    print()
    print(pabrik.kayu.tambah_bahan(30))
    print(pabrik.kaca.tambah_bahan(20))


if __name__ == "__main__":
    tampilkan_demo()
    