import pytest

from f4shion_ecommerce_django.users.models import User
from f4shion_ecommerce_django.users.tests.factories import UserFactory


@pytest.fixture(autouse=True)
def media_storage(settings, tmpdir):
    settings.MEDIA_ROOT = tmpdir.strpath


@pytest.fixture
def user(db) -> User:
    return UserFactory()
