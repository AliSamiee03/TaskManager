from django.db import models
from django.contrib.auth.models import BaseUserManager, AbstractBaseUser


class UserAccountManager(BaseUserManager):
    def create_user(self, email, name , password=None):
        """
        Creates and saves a User with the given email, name and password.
        """
        if not email :
            raise ValueError('Users must have an email address')
        else:
            user = self.model(email = self.normalize_email(email), name=name)

        user.set_password(password)
        user.save()

        return user
    
    def create_superuser(self, email, name, password=None):
        """
        Creates and saves a superuser with the given email, name and password.
        """
        user = self.create_user(email=email, name=name, password=password)
        user.is_superuser = True
        user.is_staff = True
        user.save()

        return user




class UserAccount(AbstractBaseUser):
    email = models.EmailField(verbose_name='Email Address', max_length=250, unique=True)
    name = models.CharField(max_length=50)
    is_active = models.BooleanField(default=True)
    is_staff = models.BooleanField(default=False)

    objects = UserAccountManager()

    USERNAME_FIELD = 'email'
    REQUIRED_FIELDS = ['name']

    def __str__(self):
        return self.email

    def has_perm(self, perm, obj=None):
        "Does the user have a specific permission?"
        # Simplest possible answer: Yes, always
        return True

    def has_module_perms(self, app_label):
        "Does the user have permissions to view the app `app_label`?"
        # Simplest possible answer: Yes, always
        return True



    