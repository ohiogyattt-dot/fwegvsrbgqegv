class RatingHotel:
    def __init__(self, nama_hotel, kota, rating, jumlah_ulasan, kategori="Bintang 4"):
        self.nama_hotel = nama_hotel
        self.kota = kota
        self.rating = rating
        self.jumlah_ulasan = jumlah_ulasan
        self.kategori = kategori

    def to_list(self):
        return [self.nama_hotel, self.kota, self.rating, self.jumlah_ulasan, self.kategori]

    def __str__(self):
        return f"{self.nama_hotel} ({self.kota}) - Rating: {self.rating}/5.0 ({self.jumlah_ulasan} ulasan) - {self.kategori}"


class Pengulas:
    def __init__(self, id_pengulas, nama, email):
        self.id = id_pengulas
        self.nama = nama
        self.email = email

    def to_list(self):
        return [self.id, self.nama, self.email]

    def __str__(self):
        return f"{self.nama} ({self.id}) - {self.email}"