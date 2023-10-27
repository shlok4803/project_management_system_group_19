from django.db import models
from django.contrib.auth.models import AbstractUser
from django.contrib.auth.models import AbstractBaseUser, BaseUserManager, PermissionsMixin
from django.utils import timezone
# Create your models here.

class CustomUserManager(BaseUserManager):
    def create_user(self, email, password=None, **extra_fields):
        if not email:
            raise ValueError('The Email field must be set')
        email = self.normalize_email(email)
        user = self.model(email=email, **extra_fields)
        user.set_password(password)
        user.save(using=self._db)
        return user

    def create_superuser(self, email, password=None, **extra_fields):
        extra_fields.setdefault('is_staff', True)
        extra_fields.setdefault('is_superuser', True)
        return self.create_user(email, password, **extra_fields)

class CustomUser(AbstractBaseUser, PermissionsMixin):
    first_name = models.CharField(max_length=30, blank=True)
    email = models.EmailField(unique=True)
    contact = models.CharField(max_length=12)
    is_active = models.BooleanField(default=False)
    is_staff = models.BooleanField(default=False)
    date_joined = models.DateTimeField(default=timezone.now)

    objects = CustomUserManager()

    USERNAME_FIELD = 'email'
    REQUIRED_FIELDS = []

    def __str__(self):
        return self.email


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






