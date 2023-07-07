from .serializers import SimpananSerializer
from modul.simpanan.models import Simpanan
from rest_framework import generics

class SimpananList(generics.ListCreateAPIView):
    queryset = Simpanan.objects.all()
    serializer_class = SimpananSerializer

class SimpananDetail(generics.RetrieveUpdateDestroyAPIView):
    queryset = Simpanan.objects.all()
    serializer_class = SimpananSerializer

