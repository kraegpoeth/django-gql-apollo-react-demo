import pytest
from mixer.backend.django import mixer

# enable db writes in tests
pytestmark = pytest.mark.django_db


def test_message():
    obj = mixer.blend('simple_app.Message')
    assert obj.pk > 0
