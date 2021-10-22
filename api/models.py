from django.db import models

class User(models.Model):
    user_id = models.AutoField(primary_key=True)
    username = models.CharField(max_length = 50)
    email = models.EmailField(max_length = 100)
    password = models.CharField(max_length = 200)

class Enterprise(models.Model):
    enterprise_id = models.AutoField(primary_key=True)
    user_id = models.ForeignKey('User',on_delete=models.CASCADE)
    name = models.CharField(max_length=100)
    employers = models.IntegerField(blank=False, null=False)
    electricity = models.IntegerField(blank=False, null=False)
    gas = models.IntegerField(blank=False, null=False)
    water = models.IntegerField(blank=False, null=False)