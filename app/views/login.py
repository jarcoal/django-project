from django.conf import settings
from django.contrib.auth.views import LoginView as DjangoLoginView
from django.utils.decorators import method_decorator
from ratelimit.decorators import ratelimit


class LoginView(DjangoLoginView):
    """
    Display the login form and handle the login action.
    """

    redirect_authenticated_user = True

    @method_decorator(ratelimit(key="ip", rate=settings.LOGIN_RATELIMIT_PER_SECOND))
    @method_decorator(ratelimit(key="ip", rate=settings.LOGIN_RATELIMIT_PER_HOUR))
    def post(self, *args, **kwargs):
        """If the request was ratelimited, don't allow POSTs."""

        if self.request.limited:
            return self.get(*args, **kwargs)

        return super().post(*args, **kwargs)
