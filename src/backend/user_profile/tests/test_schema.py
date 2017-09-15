import pytest
from mixer.backend.django import mixer
from django.contrib.auth.models import AnonymousUser
from django.test import RequestFactory

from .. import schema


pytestmark = pytest.mark.django_db


def test_user_type():
    instance = schema.UserType()
    assert instance


def test_resolve_current_user():
    q = schema.Query()
    req = RequestFactory().get('/')
    req.user = AnonymousUser()
    res = q.resolve_current_user(None, req, None)
    assert res is None, 'Should return None if user is not authenticated'

    user = mixer.blend('auth.User')
    req.user = user
    res = q.resolve_current_user(None, req, None)
    assert res == user, 'Should return the current user if is authenticated'
