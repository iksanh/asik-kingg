from django_enumfield import enum

class Akun(enum.Enum):
    AKTIVA = 'Aktiva'
    PASIVA = 'Pasiva'
    KOSONG = 'NULL'

class LabaRugi(enum.Enum):
    PENDAPATAN = 'PENDAPATAN'
    HPP = 'HPP'
    BIAYA = 'BIAYA'

class Pemasukan(enum.Enum):
    YA = 'Y'
    TIDAK = 'N'
    KOSONG = 'NULL'

class Pengeluaran(enum.Enum):
    YA = 'Y'
    TIDAK = 'N'
    KOSONG = 'NULL'

class Aktif(enum.Enum):
    YA = 'Y'
    TIDAK = 'N'
