from django.urls import path
# from .views import apiListUsersView
# from .views import apiDetailUserView
# from .views import apiListEnterprisesView
# from .views import apiDetailEnterpriseView

from api import views as local_views
from api.api import UserAPI


urlpatterns = [
    path('api/create_user/', UserAPI.as_view(), name = "create_user"),
    path('api/login/', local_views.login, name="login"),
]