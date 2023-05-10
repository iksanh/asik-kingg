from django.db import models
from modul.transaksi.pilihan import Opsi as opsi
from django.utils.translation import gettext_lazy as _
from modul.kas.models import Kas
from django.contrib.auth.models import User
from datetime import datetime


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

    def __str__(self) -> str:
        return self.jenis_transaksi
    
class JurnalAkun(models.Model):
    tanggal_transaksi = models.DateTimeField(verbose_name='Tanggal Transaksi', db_column='tgl_transaksi')
    dari_akun = models.ForeignKey(Akun, on_delete=models.CASCADE, db_column='dari_akun', related_name='dari_akun')
    untuk_akun = models.ForeignKey(Akun, on_delete=models.CASCADE, db_column='untuk_akun', related_name='untuk_akun')
    jumlah = models.FloatField()
    user = models.ForeignKey(User, on_delete=models.CASCADE, db_column='user_name')
    keterangan = models.CharField(max_length=255)

    class Meta:
        db_table = 'tbl_jurnal_akun'

class Angsuran(models.Model):

    keterangan = models.IntegerField(db_column='ket')
    aktif = models.CharField(max_length=2, choices=opsi.YA_TIDAK)

    class Meta:
        db_table = 'jns_angsuran'


class TransaksiKas(models.Model):
    tanggal_catat = models.DateTimeField(verbose_name='Tanggal Transaksi')
    jumlah = models.FloatField()
    keterangan = models.CharField(max_length=255)
    akun = models.CharField(max_length=50)
    dari_kas = models.ForeignKey(Kas, on_delete=models.CASCADE, db_column='dari_kas_id', related_name='dari_kas', null=True)
    untuk_kas = models.ForeignKey(Kas, on_delete=models.CASCADE, db_column='untuk_kas_id', related_name='untuk_kas', null=True)
    jenis_transaksi  = models.ForeignKey(Akun, on_delete=models.CASCADE, db_column='jns_trans')
    debit_kredit = models.CharField(max_length=1, db_column='dk', null=True)
    update_data = models.DateTimeField(default=datetime.now, blank=True)
    user = models.ForeignKey(User, on_delete=models.CASCADE, null=True, db_column='user_name')

    

