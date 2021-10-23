from django.urls import path
# from .views import apiListUsersView
# from .views import apiDetailUserView
# from .views import apiListEnterprisesView
# from .views import apiDetailEnterpriseView


from api.api import UserAPI

urlpatterns = [
    # path('users/', apiListUsersView.as_view(), name='user_list'),
    # path('users/<int:pk>', apiDetailUserView.as_view(), name='user'),
    # path('enterprises/', apiListEnterprisesView.as_view(), name='enterprise_list'),
    # path('enterprises/<int:pk>', apiDetailEnterpriseView.as_view(), name='enterprise'),
    path('api/create_user/', UserAPI.as_view(), name = "create_user"),

]