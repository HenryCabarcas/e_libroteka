from django.db import models
from datetime import date, datetime
from django.utils import timezone
from django.contrib.auth.models import AbstractBaseUser, PermissionsMixin, BaseUserManager
from django.contrib.auth.hashers import make_password


class UserManager(BaseUserManager):
    def create_user(self, username, password=None):
        """
        Creates and saves a user with the given username and password.
        """
        if not username:
            raise ValueError('Users must have an username')
        user = self.model(username=username)
        user.set_password(password)
        user.save(using=self._db)
        return user

    def create_superuser(self, username, password):
        """
        Creates and saves a superuser with the given username and password.
        """
        user = self.create_user(
            username=username, password=password,
        )
        user.is_admin = True
        user.save(using=self._db)
        return user


class User(AbstractBaseUser, PermissionsMixin):
    username = models.CharField(
        'username', max_length=20, primary_key=True, null=False)
    email = models.EmailField('email', null=False, unique=True)
    name = models.CharField('name', max_length=20, null=False, default='User')
    lastname = models.CharField(
        'lastname', max_length=25, null=False, default='User')
    password = models.CharField('password', max_length=256, null=False)
    signUp = models.DateField('signUp', default=timezone.localdate())
    lastLogin = models.DateTimeField('lastLogin', default=datetime.now())

    def save(self, **kwargs):
        some_salt = 'mMUj0DrIK6vgtdIYepkIxN'
        self.password = make_password(self.password, some_salt)
        super().save(**kwargs)

    objects = UserManager()
    USERNAME_FIELD = 'username'
