"""Database Models."""

from typing import Union
from django.db import models
from django.contrib.auth.models import (
    AbstractBaseUser, BaseUserManager, PermissionsMixin)


class UserManager(BaseUserManager):
    """Manager for users."""

    def create_user(self, email: str, password: Union[str, None] = None, **extra_fields):
        user: User = self.model(
            email=self.normalize_email(email), **extra_fields)
        user.set_password(password)
        user.save(using=self._db)
        return user


class User(AbstractBaseUser, PermissionsMixin):
    """User in the system."""
    email = models.EmailField(max_length=255, unique=True)
    name = models.CharField(max_length=255)
    is_active: models.BooleanField(default=True)
    is_staff = models.BooleanField(default=True)
    objects = UserManager()

    USERNAME_FIELD = 'email'