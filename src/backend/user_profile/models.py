from __future__ import unicode_literals
from django.db import models


class User(models.Model):
    user = models.ForeignKey('auth.User')
    name = models.TextField()
    creation_date = models.DateTimeField(auto_now_add=True)
