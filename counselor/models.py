# Django.

from django.db import models
from django.contrib.auth.models import (
    BaseUserManager, AbstractBaseUser, PermissionsMixin
)


class CounselorManager(BaseUserManager):
    def create_user(self, cpf, email, phone, first_name):
        counselor = Counselor()
        counselor.email = self.normalize_email(email)
        counselor.phone = phone
        counselor.cpf = cpf
        counselor.first_name = first_name

        counselor.save(using=self.db)

        return counselor

    def create_super_user(self, cpf, email, phone, first_name, password):
        counselor = Counselor()
        counselor.email = self.normalize_email(email)
        counselor.phone = phone
        counselor.cpf = cpf
        counselor.first_name = first_name
        counselor.set_password(password)

        counselor.save(using=self.db)

        return counselor


class Counselor(AbstractBaseUser):
    email = models.EmailField(max_length=50, unique=True)
    phone = models.CharField(max_length=10)
    first_name = models.CharField(max_length=50)
    cpf = models.CharField(max_length=50, unique=True)

    objects = CounselorManager()

    USERNAME_FIELD = 'cpf'
    REQUIRED_FIELDS = ['email', 'phone', 'first_name']
