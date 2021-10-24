
from django.urls import path
from enterprize.api import EnterprizeAPI

urlpatterns = [
    path("api/enterprize/", EnterprizeAPI.as_view(), name = "enterprize"),
]
