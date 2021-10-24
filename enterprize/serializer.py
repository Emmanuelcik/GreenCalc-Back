from rest_framework import serializers
from django.contrib.auth.models import User

class EnterprizeSerlizer(serializers.Serializer):

    id = serializers.ReadOnlyField()
    user = serializers.PrimaryKeyRelatedField(queryset=User.objects.all())
    bimestre = serializers.CharField()
    nombre = serializers.CharField(required=True)
    electricidad = serializers.FloatField()
    # agua = serializers.FloatField() 
    gas = serializers.FloatField()
    year = serializers.CharField()
    sector = serializers.CharField()

    def create(self, validated_data):
        enterprize = EnterprizeSerlizer()
        enterprize.electricidad = validated_data.get('electricidad')
        enterprize.gas = validated_data.get('gas')
        enterprize.nombre = validated_data.get('nombre')
        enterprize.year = validated_data.get('year')
        enterprize.sector = validated_data.get('sector')
        enterprize.user = validated_data.get('user')
        enterprize.bimestre = validated_data.get("bimestre")
        enterprize.save()
        return enterprize