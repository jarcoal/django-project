from django.test import TestCase as DjangoTestCase
from django.test import override_settings
from rest_framework.test import APIClient


@override_settings(
    CACHES={
        "default": {
            "BACKEND": "django.core.cache.backends.locmem.LocMemCache",
        },
    },
    CELERY_BROKER_URL="memory://localhost/",
)
class TestCase(DjangoTestCase):
    """Abstract TestCase class to be used in test suite."""

    # Allow diffs of any length to be dumped to the console
    # https://goo.gl/sLD3nT
    maxDiff = None

    @classmethod
    def setUpClass(cls):
        # Anything global that needs to be set up before running tests.
        super().setUpClass()


class APITestCase(TestCase):
    """Abstract TestCase to be used for testing API endpoints"""

    # Set our APIClient as the default client class
    client_class = APIClient
