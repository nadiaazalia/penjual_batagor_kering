class PabrikKayu:
    def __init__(self, nama):
        self.nama = nama
        self._jenis_kayu = "Jati"
        self.__stok_bahan = 120

    def produksi(self):
        return f"Produksi kayu di {self.nama}: {self._jenis_kayu} diproses menjadi ukiran, meja, dan bingkai cantik."

    def _periksa_stok(self):
        return f"Stok bahan kayu tersisa: {self.__stok_bahan} balok."

    def __tambah_stok(self, jumlah):
        self.__stok_bahan += jumlah
        return self.__stok_bahan

    def tambah_bahan(self, jumlah):
        sebelum = self.__stok_bahan
        setelah = self.__tambah_stok(jumlah)
        return f"Menambah bahan kayu: {jumlah} balok (dari {sebelum} menjadi {setelah})."
