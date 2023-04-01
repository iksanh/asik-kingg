from django_enumfield import enum

class Opsi():
    PILIHAN_AKUN = (
        ('Aktiva', 'AKTIVA'),
        ('Pasiva', 'PASIVA')
    )

    LABA_RUGI = (
        ('PENDAPATAN', 'PENDAPATAN'),
        ('HPP', 'HPP'),
        ('BIAYA', 'BIAYA'),
        ('PINJAMAN', 'PINJAMAN')
    )

    YA_TIDAK = (
        ('Y', 'YA'),
        ('N', 'TIDAK')
    )

