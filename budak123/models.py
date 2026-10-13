class PesananJoki:
    def __init__(self, nama_klien, jenis_joki, harga, status="Proses"):
        self.nama_klien = nama_klien
        self.jenis_joki = jenis_joki
        self.harga = harga
        self.status = status

    def to_list(self):
        return [self.nama_klien, self.jenis_joki, self.harga, self.status]

    def __str__(self):
        return f"{self.nama_klien} - {self.jenis_joki} (Rp{self.harga}) - {self.status}"


class Pelanggan:
    def __init__(self, id_pelanggan, nama, no_hp):
        self.id = id_pelanggan
        self.nama = nama
        self.no_hp = no_hp

    def to_list(self):
        return [self.id, self.nama, self.no_hp]

    def __str__(self):
        return f"{self.nama} ({self.id}) - {self.no_hp}"