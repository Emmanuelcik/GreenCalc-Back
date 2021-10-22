from django.db import models

class User(models.Model):
    user_id = models.AutoField(primary_key=True)
    username = models.CharField(max_length = 50, unique=True, null=False)
    email = models.EmailField(max_length = 100, null=False)
    password = models.CharField(max_length = 200, null=False)

    created = models.DateTimeField(auto_now_add=True)
    edited = models.DateTimeField(auto_now=True)

class Enterprise(models.Model):
    enterprise_id = models.AutoField(primary_key=True)
    user_id = models.ForeignKey('User',on_delete=models.CASCADE)
    name = models.CharField(max_length=100, null=False)
    employers = models.IntegerField(blank=False, null=False)
    electricity = models.IntegerField(blank=False, null=False)
    gas = models.IntegerField(blank=False, null=False)
    water = models.IntegerField(blank=False, null=False)