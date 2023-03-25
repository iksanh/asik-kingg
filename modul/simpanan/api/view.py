from .serializers import SimpananSerializer
from modul.simpanan.models import Simpanan
from django.http import Http404
# from rest_framework.views i
from rest_framework.response import Response
from rest_framework import status, generics

class SimpananList(generics.ListCreateAPIView):
    queryset = Simpanan.objects.all()
    serializer_class = SimpananSerializer

class SimpananDetail(generics.RetrieveUpdateDestroyAPIView):
    queryset = Simpanan.objects.all()
    serializer_class = SimpananSerializer

