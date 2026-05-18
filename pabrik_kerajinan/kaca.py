class PabrikKaca:
    def __init__(self, nama):
        self.nama = nama
        self._jenis_kaca = "Kaca patri"
        self.__stok_bahan = 80

    def produksi(self):
        return f"Produksi kaca di {self.nama}: {self._jenis_kaca} dipotong, dicetak, dan dirangkai menjadi lampu, jendela, dan ornamen modern."

    def _periksa_stok(self):
        return f"Stok bahan kaca tersisa: {self.__stok_bahan} lembar."

    def __tambah_stok(self, jumlah):
        self.__stok_bahan += jumlah
        return self.__stok_bahan

    def tambah_bahan(self, jumlah):
        sebelum = self.__stok_bahan
        setelah = self.__tambah_stok(jumlah)
        return f"Menambah bahan kaca: {jumlah} lembar (dari {sebelum} menjadi {setelah})."
