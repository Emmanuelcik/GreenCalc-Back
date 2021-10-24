from .serializer import UserSerializer
from django.contrib.auth.models import User
from django.db.models.deletion import RESTRICT
from rest_framework.decorators import api_view
from rest_framework.authtoken.models import Token
from django.contrib.auth.hashers import check_password
from rest_framework.response import Response

@api_view(["POST"])

def login(request):

    print(request)
    # usuario = UserSerializer
    username = request.POST.get('username')
    password = request.POST.get('password')
    # email = request.POST.get("email")

    user = User.objects.get(username=username)
    # try:
    # except User.DoesNotExist:
    #     return Response("Usuario no valido")
    
    pwd_valid = check_password(password, user.password)

    if not pwd_valid:
        return Response("Contraeña invalida")
    

    token, _ = Token.objects.get_or_create(user=user)

    print(token.key)
    return Response(token.key)