from .kayu import PabrikKayu
from .kaca import PabrikKaca

class PabrikKerajinan:
    def __init__(self, nama_pabrik):
        self.nama_pabrik = nama_pabrik
        self.kayu = PabrikKayu(f"{nama_pabrik} - Kayu")
        self.kaca = PabrikKaca(f"{nama_pabrik} - Kaca")
        self._story = "Pabrik kerajinan tumbuh dari tradisi warisan lokal dan teknik modern."

    def memproduksi(self):
        produksi_kayu = self.kayu.produksi()
        produksi_kaca = self.kaca.produksi()
        return f"--- {self.nama_pabrik} ---\n{produksi_kayu}\n{produksi_kaca}"

    def _cerita_brand(self):
        return f"{self.nama_pabrik}: {self._story}"

    def operasi_teknis(self):
        detail_kayu = self.kayu._periksa_stok()
        detail_kaca = self.kaca._periksa_stok()
        return f"{detail_kayu}\n{detail_kaca}"
