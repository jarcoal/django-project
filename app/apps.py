from django.apps import AppConfig
from django.contrib import admin


class AppConfig(AppConfig):
    name = "app"

    def ready(self):
        from django_otp.admin import OTPAdminSite

        from app import signals  # noqa: F401

        admin.site.__class__ = OTPAdminSite
