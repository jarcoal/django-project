from django.conf import settings

from .factories import UserFactory
from .test_case import TestCase
from app.models import User
from django.urls import reverse_lazy
from allauth.account.views import LoginView


class LoginViewTests(TestCase):
    MOCK_PASSWORD = "MOCK_PASSWORD"
    VIEW_URL = reverse_lazy("account_login")

    @classmethod
    def setUpTestData(cls):
        cls.user = UserFactory.create()
        cls.user.set_password(cls.MOCK_PASSWORD)
        cls.user.save(update_fields=["password"])

    def test_get(self):
        """Make sure that we can fetch the login page"""

        # Fetch the login page
        resp = self.client.get(self.VIEW_URL)

        # Make sure we got a 200
        self.assertEqual(resp.status_code, 200)

    def test_post(self):
        """Check that we can submit the login form"""

        # Make a good request and see if it redirects to the login redirect URL
        resp = self.client.post(
            self.VIEW_URL,
            {
                "login": self.user.email,
                "password": self.MOCK_PASSWORD,
            },
        )

        self.assertRedirects(
            resp,
            settings.LOGIN_REDIRECT_URL,
            fetch_redirect_response=False,
        )

    def test_login_bad_creds(self):
        """Check that bad logins are rejected"""

        resp = self.client.post(
            self.VIEW_URL,
            {
                "login": self.user.email,
                "password": "invalidpass",
            },
        )

        # Make sure they weren't redirected
        self.assertEqual(resp.status_code, 200)

        # Make sure we got the expected form error
        self.assertFormError(
            resp,
            "form",
            None,
            LoginView.form_class.error_messages["email_password_mismatch"],
        )
