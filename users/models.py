from django.db import models
from django.conf import settings
from django.conf import *

class Email_store(models.Model):
    auto_increment_id = models.AutoField(primary_key=True)
    mEmail = models.CharField(max_length=254)
    subscribed_at = models.DateField(auto_now_add=True)

    