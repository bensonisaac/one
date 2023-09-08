from django.db import models

class Info(models.Model):
    slack_name = models.CharField(max_length=200)
    track = models.CharField(max_length=200)