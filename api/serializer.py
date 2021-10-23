from rest_framework import serializers
from django.contrib.auth.models import User

class UserSerializer(serializers.Serializer):
    id = serializers.ReadOnlyField()
    username = serializers.CharField()
    password = serializers.CharField()
    email = serializers.CharField()

    def create(self, validated_data):
        user = User()
        user.username = validated_data.get('username')
        user.set_password(validated_data.get('password'))
        user.email = validated_data.get('email')
        user.save()
        return user

    def validateUsername(self, data):
        user = User.objects.filter(username = data)
        if len(user) != 0:
            raise serializers.ValidationError("Este usuario ya existe, Ingrese uno nuevo")
        else:
            return data
    
