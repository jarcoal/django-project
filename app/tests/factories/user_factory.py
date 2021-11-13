import factory
import pytz
from app.models import User
from django.conf import settings


class UserFactory(factory.django.DjangoModelFactory):
    class Meta:
        model = User

    first_name = factory.Faker("first_name")
    last_name = factory.Faker("last_name")
    email = factory.Sequence(lambda n: "user+%d@example.com" % n)
    image = factory.Faker("url")
    timezone = pytz.UTC
    language = settings.LANGUAGE_CODE
