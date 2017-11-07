from rest_framework import serializers
from HKDataBase.models import HKData

class HKDataSerializer(serializers.ModelSerializer):
    class Meta :
        model = HKData
        fields = ('title','description','type','section','lat','lon','image','created','updated')

    def create(self, validated_data):
        return HKData.objects.create(**validated_data)