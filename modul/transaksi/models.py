from django.db import models
from modul.transaksi.pilihan import Opsi as opsi
from django.utils.translation import gettext_lazy as _


# Create your models here.
#model untuk tabel jns_akun dan  jns angsuran

class Akun(models.Model):

    kode_aktiva = models.CharField(max_length=5, db_column='kd_aktiva')
    jenis_transaksi = models.CharField(max_length=50, db_column='jns_trans')
    akun = models.CharField(max_length=15,  null=True, choices=opsi.PILIHAN_AKUN)
    laba_rugi = models.CharField(max_length=15, choices=opsi.LABA_RUGI, null=True)
    pemasukan = models.CharField(max_length=1, choices=opsi.YA_TIDAK , null=True)
    pengeluaran = models.CharField(max_length=1, choices=opsi.YA_TIDAK , null=True)
    aktif = models.CharField(max_length=1, choices=opsi.YA_TIDAK, null=False)

    class Meta:
        db_table = 'jns_akun'

class Angsuran(models.Model):

    keterangan = models.IntegerField(db_column='ket')
    aktif = models.CharField(max_length=2, choices=opsi.YA_TIDAK)

    class Meta:
        db_table = 'jns_angsuran'


