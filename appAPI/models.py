from django.db import models

# Create your models here.


class Penulis(models.Model):
    nama = models.CharField(max_length=50)
    asal = models.CharField(max_length=50)
    kontak = models.CharField(max_length=50)

    def __str__(self):
        return f'{self.id}. {self.nama}-{self.asal}'


class Buku(models.Model):
    judul = models.CharField(max_length=250)
    tahun = models.CharField(max_length=50)
    penerbit = models.CharField(max_length=50)
    penulis = models.ForeignKey(Penulis, on_delete=models.CASCADE)

    def __str__(self):
        return f'{self.id}. {self.judul}'
