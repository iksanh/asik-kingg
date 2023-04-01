from django.db import models

# Create your models here.
class Pinjaman(models.Model):
    nama = models.CharField(max_length=255, db_column='nm_barang'),
    type = models.CharField(max_length=50),
    merek = models.CharField(max_length=50, db_column='merk'),
    harga = models.FloatField(),
    jumlah_barang = models.IntegerField(db_column='jml_brg'),
    keterangan = models.CharField(max_length=255, db_column='ket')


    class Meta:
        db_table = 'tbl_barang'