# Generated by Django 3.2 on 2023-05-10 22:08

import datetime
from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('kas', '0002_kas_pinjaman'),
        ('member', '0003_auto_20230430_1958'),
        ('simpanan', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='TransaksiSetoranSimpanan',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('tanggal_transaksi', models.DateTimeField(db_column='tgl_transaksi', verbose_name='Tanggal Transaksi')),
                ('jumlah', models.FloatField()),
                ('keterangan', models.CharField(choices=[('Setoran', 'Setoran'), ('Bunga', 'Bunga')], default='Setoran', max_length=255)),
                ('akun', models.CharField(max_length=255)),
                ('dk', models.CharField(max_length=255)),
                ('update_data', models.DateTimeField(blank=True, default=datetime.datetime.now)),
                ('penyetor', models.CharField(db_column='nama_penyetor', max_length=255, verbose_name='Nama Penyetor')),
                ('nomor_identitas', models.CharField(db_column='no_identitas', max_length=100, verbose_name='Nomor Identitias')),
                ('alamat', models.CharField(max_length=255)),
                ('anggota', models.ForeignKey(db_column='anggota_id', on_delete=django.db.models.deletion.CASCADE, to='member.member', verbose_name='Nama Anggota')),
                ('jenis_transaksi', models.ForeignKey(db_column='jenis_id', on_delete=django.db.models.deletion.CASCADE, to='simpanan.simpanan', verbose_name='Jenis Simpanan')),
                ('kas', models.ForeignKey(db_column='kas_id', on_delete=django.db.models.deletion.CASCADE, to='kas.kas', verbose_name='Simpan ke Kas')),
                ('user', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL)),
            ],
            options={
                'db_table': 'tbl_trans_sp',
            },
        ),
    ]
