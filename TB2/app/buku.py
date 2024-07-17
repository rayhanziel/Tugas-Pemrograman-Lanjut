class Buku:
    def __init__(self, judul, penulis, penerbit, tahun_terbit, konten, iktisar):
        self.judul = judul
        self.penulis = penulis
        self.penerbit = penerbit
        self.tahun_terbit = tahun_terbit
        self.konten = konten if isinstance(konten, list) else konten.split(",")
        self.iktisar = iktisar

    def read(self, halaman):
        if halaman <= 0 or halaman > len(self.konten):
            return "Nomor halaman tidak valid"
        return self.konten[:halaman]

    def __str__(self):
        return f"{self.judul} by {self.penulis}"
