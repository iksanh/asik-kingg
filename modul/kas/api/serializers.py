from rest_framework import serializers
from modul.kas.models import Kas

class KasSerializer(serializers.ModelSerializer):
    class Meta:
        model = Kas
        fields = '__all__'