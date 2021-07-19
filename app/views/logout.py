from django.contrib.auth.views import LogoutView as DjangoLogoutView


class LogoutView(DjangoLogoutView):
    """
    Log out the user and send on their way
    """
