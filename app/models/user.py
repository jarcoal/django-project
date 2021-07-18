from django.db import models
from django.conf import settings
from django.contrib.auth.models import (
    AbstractUser,
    BaseUserManager,
)
from timezone_field import TimeZoneField


class UserManager(BaseUserManager):
    """Manager to create users with emails as USERNAME_FIELD"""

    def _create_user(self, email, password, is_staff, is_superuser, **kwargs):
        """
        Creates and saves a User with the given email and password.
        """
        user = self.model(
            email=self.normalize_email(email),
            is_staff=is_staff,
            is_active=True,
            is_superuser=is_superuser,
        )

        user.set_password(password)
        user.save(using=self._db)

        return user

    def create_user(self, **kwargs):
        return self._create_user(is_staff=False, is_superuser=False, **kwargs)

    def create_superuser(self, **kwargs):
        return self._create_user(is_staff=True, is_superuser=True, **kwargs)


class User(AbstractUser):
    """
    Users within the Django authentication system are represented by this
    model.

    Email and password are required. Other fields are optional.
    """

    USERNAME_FIELD = EMAIL_FIELD = "email"
    REQUIRED_FIELDS = []

    objects = UserManager()

    # This will remove Django's default username field.
    # We'll use email instead.
    username = None

    email = models.EmailField(unique=True)

    image = models.URLField(blank=True, null=True)

    timezone = TimeZoneField(null=True, blank=True)
    language = models.CharField(max_length=7, default="en", choices=settings.LANGUAGES)

    email_verified_at = models.DateTimeField(null=True, blank=True)
    password_updated_at = models.DateTimeField(null=True, blank=True)
