from django.db import models

# Create your models here.

class Pekerjaan(models.Model):
    nama = models.CharField(max_length=150)

    class Meta:
        db_table = 'pekerjaan'

    def __str__(self) -> str:
        return self.nama