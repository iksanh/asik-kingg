from django.urls import path
from modul.transaksi import views as view
from modul.transaksi.view_pemasukan import (PemasukanKasView, PemasukanKasCreate, PemasukanKasUpdate, delete_pemasukan)
from modul.transaksi.view_pengeluaran import (PengeluaranView, PengeluaranKasUpdate, PengeluaranKasCreate, delete_pengeluaran)
from modul.transaksi.view_transfer import (TransferView, TransferKasCreate , TransferKasUpdate, delete_transfer, ReportTransferKas, TransferJurnalAkunView, TransferJurnalCreate, TransferJurnalUpdate, delete_jurnal_akun, ReportJurnalAkun)


urlpatterns = [
    path('', view.AkunView.as_view(), name='list-akun'),
    path('create/', view.create_akun, name='create-akun'),
    path('edit/<int:id>', view.edit_akun, name='edit-akun'),
    path('delete/<int:id>', view.delete_akun, name='delete-akun'),

    ## url for angsuran 
    path('angsuran/', view.AngsuranView.as_view(), name='list-angsuran'),
    path('create/angsuran', view.AngsuranCreate.as_view(), name='create-angsuran'),
    path('edit/angsuran/<int:pk>', view.AngsuranUpdate.as_view(), name='edit-angsuran'),
    path('delete/angsuran/<int:id>', view.angsuran_delete, name='delete-angsuran'),


    ## url for pemasukan 
    path('pemasukan_kas/', PemasukanKasView.as_view(template_name = 'transaksi/pemasukan_kas/list_pemasukan_kas.html' ), name='list-pemasukan_kas'),
    path('create/pemasukan_kas', PemasukanKasCreate.as_view(template_name = 'transaksi/pemasukan_kas/create_pemasukan_kas.html'), name='create-pemasukan_kas'),
    path('edit/pemasukan_kas/<int:pk>', PemasukanKasUpdate.as_view(template_name = 'transaksi/pemasukan_kas/create_pemasukan_kas.html'), name='edit-pemasukan_kas'),
    path('delete/pemasukan_kas/<int:id>', delete_pemasukan, name='delete-pemasukan_kas'),
    
    ## url for pengeluaran kas
    path('pengeluaran_kas/', PengeluaranView.as_view(template_name = 'transaksi/pengeluaran_kas/list_pengeluaran_kas.html' ), name='list-pengeluaran_kas'),
    path('create/pengeluaran_kas', PengeluaranKasCreate.as_view(template_name = 'transaksi/pengeluaran_kas/create_pengeluaran_kas.html'), name='create-pengeluaran_kas'),
    path('edit/pengeluaran_kas/<int:pk>', PengeluaranKasUpdate.as_view(template_name = 'transaksi/pengeluaran_kas/create_pengeluaran_kas.html'), name='edit-pengeluaran_kas'),
    path('delete/pengeluaran_kas/<int:id>', delete_pengeluaran, name='delete-pengeluaran_kas'),


    ## url for transfer kas
    path('transfer_kas/', TransferView.as_view(template_name = 'transaksi/transfer_kas/list_transfer_kas.html' ), name='list-transfer_kas'),
    path('create/transfer_kas', TransferKasCreate.as_view(template_name = 'transaksi/transfer_kas/create_transfer_kas.html'), name='create-transfer_kas'),
    path('edit/transfer_kas/<int:pk>', TransferKasUpdate.as_view(template_name = 'transaksi/transfer_kas/create_transfer_kas.html'), name='edit-transfer_kas'),
    path('delete/transfer_kas/<int:id>', delete_transfer, name='delete-transfer_kas'),
    # path('laporan/transfer_kas', generate_pdf, name='laporan-transfer_kas' ),
    path('report/transfer_kas/', ReportTransferKas.as_view(), name='report-transfer_kas' ),


    ## url for transfer jurnal akun
    path('jurnal_akun/', TransferJurnalAkunView.as_view(template_name = 'transaksi/jurnal_akun/list_transfer_jurnal.html' ), name='list-jurnal_akun'),
    path('create/jurnal_akun', TransferJurnalCreate.as_view(template_name = 'transaksi/transfer_kas/create_transfer_kas.html'), name='create-jurnal_akun'),
    path('edit/jurnal_akun/<int:pk>', TransferJurnalUpdate.as_view(template_name = 'transaksi/transfer_kas/create_transfer_kas.html'), name='edit-jurnal_akun'),
    path('delete/jurnal_akun/<int:id>', delete_jurnal_akun, name='delete-jurnal_akun'),
    path('report/jurnal_akun/', ReportJurnalAkun.as_view(), name='report-jurnal_akun' ),



]