from django.db import models
from django.utils.translation import gettext_lazy as _


class Kas(models.Model):
    class Opsi(models.TextChoices):
        YA = 'Y', _('Y')
        TIDAK = 'N',_('N')
    nama = models.CharField(max_length=255)
    aktif = models.CharField(max_length=2, choices=Opsi.choices)
    simpanan = models.CharField(max_length=2, choices=Opsi.choices, db_column='tmpl_simpan')
    penarikan = models.CharField(max_length=2, choices=Opsi.choices, db_column='tmpl_penarikan')
    pinjaman = models.CharField(max_length=2, choices=Opsi.choices, db_column='tmpl_pinjaman', default='Y')
    bayar = models.CharField(max_length=2, choices=Opsi.choices, db_column='tmpl_bayar')
    pemasukan = models.CharField(max_length=2, choices=Opsi.choices, db_column='tmpl_pemasukan')
    pengeluaran = models.CharField(max_length=2, choices=Opsi.choices, db_column='tmpl_pengeluaran')
    transfer = models.CharField(max_length=2, choices=Opsi.choices, db_column='tmpl_transfer')

    class Meta:
        db_table = 'nama_kas_tbl'


    def __str__(self):
        return self.nama


