from django.db import models
from django.utils.translation import gettext_lazy as _
from modul.member.models import Member
from modul.transaksi.models import Kas
from datetime import datetime
from django.contrib.auth.models import User



class Simpanan(models.Model):
    class Opsi(models.TextChoices):
        YA = 'Y', _('YA')
        TIDAK = 'N',_('TIDAK')

    jenis_simpanan = models.CharField(max_length=30, db_column='jns_simpanan')
    jumlah = models.BigIntegerField()
    tampil = models.CharField(max_length=2, choices=Opsi.choices)
    keterangan = models.CharField(max_length=255, db_column='ket')

    class Meta:
        db_table = 'jns_simpanan'

    def __str__(self) -> str:
        return self.jenis_simpanan

class TransaksiSetoranSimpanan(models.Model):
    class Keterangan(models.TextChoices):
        Setoran = 'Setoran', _('Setoran')
        Bunga = 'Bunga',_('Bunga')
    tanggal_transaksi = models.DateTimeField(verbose_name='Tanggal Transaksi', db_column='tgl_transaksi')   
    anggota = models.ForeignKey(Member, on_delete=models.CASCADE, db_column='anggota_id', verbose_name='Nama Anggota')
    jenis_transaksi = models.ForeignKey(Simpanan, on_delete=models.CASCADE, verbose_name='Jenis Simpanan', db_column='jenis_id')
    jumlah = models.FloatField(verbose_name='Jumlah Simpanan')
    keterangan = models.CharField(max_length=255, choices=Keterangan.choices, default='Setoran')
    akun = models.CharField(max_length=255)
    dk = models.CharField(max_length=255)
    kas = models.ForeignKey(Kas, on_delete=models.CASCADE, db_column='kas_id', verbose_name='Simpan ke Kas')
    update_data = models.DateTimeField(default=datetime.now, blank=True)
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    penyetor = models.CharField(max_length=255, db_column='nama_penyetor', verbose_name='Nama Penyetor')
    nomor_identitas = models.CharField(max_length=100, db_column='no_identitas', verbose_name='Nomor Identitias')
    alamat = models.CharField(max_length=255)

    
    class Meta:
        db_table = 'tbl_trans_sp'
