# Generated by Django 3.2 on 2023-03-22 03:49

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('transaksi', '0004_angsurang'),
    ]

    operations = [
        migrations.RenameModel(
            old_name='Angsurang',
            new_name='Angsuran',
        ),
        migrations.AlterModelTable(
            name='angsuran',
            table='jns_angsuran',
        ),
    ]
