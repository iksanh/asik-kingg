from django.db import models
from django.contrib.auth.models import User
from modul.crud_params import Opsi
from modul.pekerjaan.models import Pekerjaan
from modul.settings.models import Departement

# class User(AbstractUser):
#     pass

class Member(models.Model):
    nama = models.CharField(max_length=200)
    identitas = models.CharField(max_length=255, null=True)
    jenis_kelamin = models.CharField(max_length=2, db_column='jk', null=True, choices=Opsi.JENIS_KELAMIN)
    tempat_lahir = models.CharField(max_length=255, db_column='tmp_lahir', null=True)
    tanggal_lahir = models.DateField(db_column='tgl_lahir', null=True)
    status = models.CharField(max_length=50, blank=True, choices=Opsi.STATUS_PERKAWINAN)
    agama = models.CharField(max_length=30, blank=False, choices=Opsi.AGAMA)
    departement = models.ForeignKey(Departement, on_delete=models.CASCADE, db_index=True, name='departement', null=True)
    pekerjaan = models.ForeignKey(Pekerjaan, on_delete=models.CASCADE, null=True)
    alamat = models.TextField(blank=True)
    kota = models.CharField(max_length=255, blank=True)
    nomor_telpon = models.CharField(max_length=100, db_column='notelp', blank=True)
    aktif = models.BooleanField(default=True, blank=True)
    jabatan  = models.IntegerField(blank=True, null=True)
    photo = models.FileField(upload_to='static/images/profiles', blank=True, null=True)
    user = models.OneToOneField(User, on_delete=models.CASCADE, null=True, blank=True)

    class Meta:
        db_table = 'tbl_anggota'


    def __str__(self) -> str:
        return f'{self.nama}'