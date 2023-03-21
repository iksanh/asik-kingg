from django.db import models
from django.utils.translation import gettext_lazy as _



class Simpanan(models.Model):
    class Opsi(models.TextChoices):
        YA = 'Y', _('Y')
        TIDAK = 'N',_('N')

    jenis_simpanan = models.CharField(max_length=30, db_column='jns_simpanan')
    jumlah = models.BigIntegerField()
    tampil = models.CharField(max_length=2, choices=Opsi.choices)
    keterangan = models.CharField(max_length=255, db_column='ket')

    class Meta:
        db_table = 'jns_simpanan'


