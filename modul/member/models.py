from django.db import models

class Member(models.Model):
    nama = models.CharField(max_length=200)
    identitas = models.CharField(max_length=255, null=True)
    jenis_kelamin = models.CharField(max_length=2, db_column='jk', null=True)
    tempat_lahir = models.CharField(max_length=255, db_column='tmp_lahir', null=True)
    tanggal_lahir = models.DateField(db_column='tgl_lahir', null=True)
    status = models.CharField(max_length=50, blank=True)
    agama = models.CharField(max_length=30, blank=True)
    departement = models.CharField(max_length=255, blank=True)
    pekerjaan = models.CharField(max_length=30, blank=True)
    alamat = models.TextField(blank=True)
    kota = models.CharField(max_length=255, blank=True)
    nomor_telpon = models.CharField(max_length=100, db_column='notelp', blank=True)
    aktif = models.BooleanField(default=True, blank=True)
    jabatan  = models.IntegerField(blank=True, null=True)
    photo = models.FileField(upload_to='uploads', blank=True, null=True)

    class Meta:
        db_table = 'tbl_anggota'

