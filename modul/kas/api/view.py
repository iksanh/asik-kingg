from .serializers import KasSerializer
from modul.kas.models import Kas
from rest_framework import status, generics

class KasList(generics.ListCreateAPIView):
    queryset = Kas.objects.all()
    serializer_class = KasSerializer

class KasDetail(generics.RetrieveUpdateDestroyAPIView):
    queryset = Kas.objects.all()
    serializer_class = KasSerializer

