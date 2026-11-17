from django.db import models
from django.contrib.auth.models import AbstractUser
# Create your models here.

class User(AbstractUser):
    user-id = models.autoField(primary_key=True)
    username = models.charField(max_length=150, unique=True)
    password = models.charField(max_length=128)

    USERNAME_FIELD = 'username'

    class Meta:
        db_table = 'users'
        verbose_name = 'User'
        verbose_name_plural = 'Users'

class Role(models.Model):
    PERMISSION_CHOICES = [
        ('0', 'No Access'),
        ('1', 'View Only'),
        ('2', 'create and modify'),
    ]

    role_name = models.CharField(max_length=50, primary_key=True)
    customers = models.CharField(choices=PERMISSION_CHOICES, default='0')
    suppliers = models.CharField( choices=PERMISSION_CHOICES, default='0')
    materials = models.CharField( choices=PERMISSION_CHOICES, default='0')
    purchases = models.CharField(choices=PERMISSION_CHOICES, default='0')
    sales = models.CharField( choices=PERMISSION_CHOICES, default='0')
    inventory = models.CharField(max_length=1, choices=PERMISSION_CHOICES, default='0')
    accounting = models.CharField( choices=PERMISSION_CHOICES, default='0')
    reporting = models.CharField( choices=PERMISSION_CHOICES, default='0')


    class Meta:
        db_table = 'roles'
        verbose_name = 'Role'
        verbose_name_plural = 'Roles'

    def __str__(self):
        return self.role_name

class UserRole(models.Model):
    user_id = models.ForeignKey(User, on_delete=models.CASCADE)
    role = models.ForeignKey(Role, on_delete=models.CASCADE)

    class Meta:
        db_table = 'user_roles'
        verbose_name = 'User Role'
        verbose_name_plural = 'User Roles'
        unique_together = ('user_id', 'role')


    def __str__(self):
        return f"{self.user.username} - {self.role.role_name}"  