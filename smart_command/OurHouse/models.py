from django.db import models

class addation_user(models.Model):
    UIN = models.CharField(max_length=30, blank=True)
    telegram = models.CharField(max_length=30, blank=True)


