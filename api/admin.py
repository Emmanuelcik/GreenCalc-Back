from django.contrib import admin
from .models import User
from .models import Enterprise

admin.site.register(User)
admin.site.register(Enterprise)

