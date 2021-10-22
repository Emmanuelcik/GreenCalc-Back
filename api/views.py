from django.views import View
from .models import User
from .models import Enterprise
from django.http import JsonResponse
from django.forms.models import model_to_dict

class apiListUsersView(View):
    def get(self, request):
        uList = User.objects.all()
        return JsonResponse(list(uList.values()), safe=False)

class apiDetailUserView(View):
    def get(self, request, pk):
        user = User.objects.get(pk=pk)
        return JsonResponse(model_to_dict(user))

class apiListEnterprisesView(View):
    def get(self, request):
        eList = Enterprise.objects.all()
        return JsonResponse(list(eList.values()), safe=False)

class apiDetailEnterpriseView(View):
    def get(self, request, pk):
        enterprise = Enterprise.objects.get(pk=pk)
        return JsonResponse(model_to_dict(enterprise))