import zoneinfo

import factory
from django.conf import settings

from app.models import User


class UserFactory(factory.django.DjangoModelFactory):
    class Meta:
        model = User

    first_name = factory.Faker("first_name")
    last_name = factory.Faker("last_name")
    email = factory.Sequence(lambda n: "user+%d@example.com" % n)
    image = factory.Faker("url")
    timezone = zoneinfo.ZoneInfo("UTC")
    language = settings.LANGUAGE_CODE
