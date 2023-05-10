from django.db import models

# Create your models here.

class Pemasok(models.Model):
    nama = models.CharField(max_length=100, blank=False)
    alamat = models.CharField(max_length=255)
    nomor_telpon = models.CharField(max_length=15, db_column='no_telp')
    aktif = models.BooleanField(max_length=10)
    keterangan = models.CharField(max_length=255, db_column='ket')


    class Meta:
        db_table = 'tbl_pemasok'