from .serializers import AkunSerializer, AngsuranSerializer
from modul.transaksi.models import Akun, Angsuran
from rest_framework import status, generics

class AkunList(generics.ListCreateAPIView):
    queryset = Akun.objects.all()
    serializer_class = AkunSerializer

class AkunDetail(generics.RetrieveUpdateDestroyAPIView):
    queryset = Akun.objects.all()
    serializer_class = AkunSerializer

class AngsuranList(generics.ListCreateAPIView):
    queryset =  Angsuran.objects.all()
    serializer_class = AngsuranSerializer

class AngsuranDetail(generics.RetrieveUpdateDestroyAPIView):
    queryset = Angsuran.objects.all()
    serializer_class = AngsuranSerializer
