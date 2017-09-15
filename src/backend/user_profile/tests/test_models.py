import pytest
from mixer.backend.django import mixer

# We need to do this so that writing to the DB is possible in our tests.
pytestmark = pytest.mark.django_db


def test_user():
    obj = mixer.blend('user_profile.User')
    assert obj.pk > 0
