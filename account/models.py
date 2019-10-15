from django.db import models
from django.contrib.auth.models import User

# Create your models here.
class Profile(models.Model) :
    # 기존의 User Model과 OneToOne 으로 연결
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    nickname = models.TextField(max_length=10)
    phonenumber = models.CharField(verbose_name="phone number", max_length=10)
    birthdate = models.DateField(verbose_name="birth date", unique=False)
    accountnumber = models.CharField(verbose_name="account number", max_length=16)
    region = models.TextField(max_length=10, unique=False, null=True)
    reliability = models.DecimalField(max_digits=5,decimal_places=2, unique=False, null=True) # ~999
    point = models.DecimalField(max_digits=5,decimal_places=2, unique=False, null=True) # ~999


