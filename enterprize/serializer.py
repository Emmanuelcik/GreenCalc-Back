from rest_framework import serializers
from django.contrib.auth.models import User

class EnterprizeSerlizer(serializers.Serializer):
    id = serializers.ReadOnlyField()
    user = serializers.PrimaryKeyRelatedField(queryset=User.objects.all())
    nombre = serializers.CharField(required=True)
    noEmpleados = serializers.IntegerField()
    electricidad = serializers.FloatField()
    agua = serializers.FloatField()
    gas = serializers.FloatField()
