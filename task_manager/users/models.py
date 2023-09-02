from django.db import models
from django.contrib.auth.models import User

# Create your models here.

""" class TimestampedModel(models.Model):
    #An abstract model with a pair of timestamps.

    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    class Meta:
        abstract = True


class UserModel(User, TimestampedModel):
    #A task manager user.
 """
