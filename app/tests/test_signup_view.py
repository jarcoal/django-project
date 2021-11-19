from django.conf import settings

from .factories import UserFactory
from .test_case import TestCase
from app.models import User
from django.urls import reverse_lazy


class SignupViewTests(TestCase):
    VIEW_URL = reverse_lazy("account_signup")

    def test_get(self):
        """Make sure that we can fetch the signup page"""

        # Fetch the signup page
        resp = self.client.get(self.VIEW_URL)

        # Make sure we got a 200
        self.assertEqual(resp.status_code, 200)

    def test_post(self):
        """Check that we can submit the signup form"""

        # Get some data to use for the signup
        user_attrs = UserFactory.build()
        MOCK_PASSWORD = "MOCK_PASSWORD"

        # Attempt the signup
        resp = self.client.post(
            self.VIEW_URL,
            {
                "email": user_attrs.email,
                "password1": MOCK_PASSWORD,
            },
        )

        # Check that the user was created
        self.assertTrue(User.objects.filter(email=user_attrs.email).exists())

        # Check that the user is redirected correctly.
        self.assertRedirects(
            resp,
            settings.LOGIN_REDIRECT_URL,
            fetch_redirect_response=False,
        )
