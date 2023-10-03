from django.db import models
from django.contrib.auth.models import AbstractUser
# Create your models here.

class CustomUser(AbstractUser):
    email = models.EmailField(unique=True)
    contact = models.CharField(max_length=12)

class owner(CustomUser):
    company_name = models.CharField(max_length=30, null=True, blank=False)
    class Meta:
        verbose_name = "Owner-User"
        verbose_name_plural = "Owner-Users" 

class manager(CustomUser):
    company_name = models.ForeignKey(owner, on_delete=models.CASCADE, null=True, blank=False)
    class Meta:
        verbose_name = "Manager-User"
        verbose_name_plural = "Manager-Users" 

class employee(CustomUser):
    company_name = models.ForeignKey(owner, on_delete=models.CASCADE, null=True, blank=False)
    class Meta:
        verbose_name = "Employee-User"
        verbose_name_plural = "Employee-Users" 






