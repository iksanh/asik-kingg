from django.db import models

# Create your models here.

class Barang(models.Model):
    nama = models.CharField(max_length=255)
    class Meta:
        db_table = 'barang_real'
