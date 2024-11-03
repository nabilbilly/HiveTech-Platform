from django.db import models
from django.db import models
from django.conf import settings

class UserProfile(models.Model):
    user = models.OneToOneField(settings.AUTH_USER_MODEL, on_delete=models.CASCADE)
    has_logged_in = models.BooleanField(default=False)

    def __str__(self):
        return self.user.username

from django.contrib.auth.models import User
from django.db import models

User.add_to_class('first_login', models.BooleanField(default=True))
