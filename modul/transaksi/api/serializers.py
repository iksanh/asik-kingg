from rest_framework import serializers
from modul.transaksi.models import Akun, Angsuran

class AkunSerializer(serializers.ModelSerializer):
    class Meta:
        model = Akun
        fields = '__all__'

class AngsuranSerializer(serializers.ModelSerializer):
    class Meta:
        model = Angsuran
        fields = '__all__'