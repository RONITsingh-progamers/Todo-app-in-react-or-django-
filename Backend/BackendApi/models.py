from django.db import models

# Create your models here.

class Plan(models.Model):
    item = models.CharField(max_length=500)