from app.utils.ratelimit import ip_cache_key
from django.conf import settings
from django.contrib.auth.views import LoginView as DjangoLoginView
from django.utils.decorators import method_decorator
from ratelimit.decorators import ratelimit


@method_decorator(
    ratelimit(
        key=ip_cache_key,
        rate=settings.LOGIN_RATELIMIT_PER_SECOND,
        method="POST",
        block=False,
    ),
    name="post",
)
@method_decorator(
    ratelimit(
        key=ip_cache_key,
        rate=settings.LOGIN_RATELIMIT_PER_HOUR,
        method="POST",
        block=False,
    ),
    name="post",
)
class LoginView(DjangoLoginView):
    """
    Display the login form and handle the login action.
    """

    redirect_authenticated_user = True

    def form_valid(self, form):
        """
        Check the rate-limiter before allowing a form-submission to proceed
        """

        # If we are rate-limited, follow the invalid form.
        if self.request.limited:
            return self.form_invalid(form)

        return super().form_valid(form)
