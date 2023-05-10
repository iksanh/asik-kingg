from django.db import models

class Settings(models.Model):
    opsi_key =  models.CharField(max_length=100, verbose_name='Keterangan')
    opsi_val = models.CharField(max_length=150, verbose_name='Deskripsi')

    class Meta:
        db_table = 'tbl_setting'
class Departement(models.Model):
    nama_departement = models.CharField(max_length=150)

    class Meta:
        db_table = 'departement'

    def __str__(self):
        return self.nama_departement

class FileRat(models.Model):
    nama = models.CharField(max_length=255, db_column='nama_file')
    file = models.FileField(upload_to='dokumen/file_rat', db_column='file_rat')

