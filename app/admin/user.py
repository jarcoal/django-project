from django.contrib import admin
from django.contrib.auth.admin import UserAdmin as BaseUserAdmin
from django.contrib.auth.forms import UserCreationForm as BaseUserCreationForm
from django.contrib.humanize.templatetags.humanize import naturaltime
from django.urls import reverse
from django.utils.safestring import mark_safe
from app.models import User


class UserCreationForm(BaseUserCreationForm):
    class Meta:
        model = User
        fields = (
            "first_name",
            "last_name",
            "timezone",
            "language",
            "email",
        )


@admin.register(User)
class UserAdmin(BaseUserAdmin):
    save_on_top = True
    add_form = UserCreationForm

    actions = []

    add_fieldsets = (
        (
            None,
            {
                "classes": ("wide",),
                "fields": (
                    "email",
                    "first_name",
                    "last_name",
                    "timezone",
                    "language",
                    "password1",
                    "password2",
                ),
            },
        ),
    )

    ordering = ("-date_joined",)

    readonly_fields = ("date_joined",)

    list_display = (
        "email",
        "first_name",
        "last_name",
        "language",
        "timezone",
        "relative_last_login",
        "relative_date_joined",
    )

    search_fields = ("email", "first_name", "last_name")

    def relative_last_login(self, user):
        return naturaltime(user.last_login)

    relative_last_login.short_description = "Last Login"
    relative_last_login.admin_order_field = "last_login"

    def relative_date_joined(self, user):
        return naturaltime(user.date_joined)

    relative_date_joined.short_description = "Date Joined"
    relative_date_joined.admin_order_field = "date_joined"

    fieldsets = (
        (
            "Personal",
            {
                "fields": (
                    "first_name",
                    "last_name",
                    "email",
                    "image",
                    "timezone",
                    "language",
                    "password",
                    "date_joined",
                )
            },
        ),
        (
            "Permissions",
            {
                "fields": (
                    "is_active",
                    "is_staff",
                    "is_superuser",
                    "groups",
                    "user_permissions",
                ),
            },
        ),
        (
            "Important Dates",
            {
                "fields": (
                    "last_login",
                    "password_updated_at",
                    "email_verified_at",
                )
            },
        ),
    )
