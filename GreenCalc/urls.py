from django.contrib import admin
from django.urls import path, include
from api.api import UserAPI
from enterprize.api import EnterprizeAPI
from api import views as api_views

urlpatterns = [
    # path('admin/', admin.site.urls),
    # path('api/',include('api.urls')),
    path('api/create_user/', UserAPI.as_view(), name = "create_user"),
    path("api/enterprize/", EnterprizeAPI.as_view(), name = "enterprize"),
    path('api/login/', api_views.login, name="login"),
]
