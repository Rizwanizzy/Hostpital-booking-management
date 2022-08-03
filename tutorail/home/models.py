from django.db import models


# Create your models here.
class departments(models.Model):
    dept_name = models.CharField(max_length=50)
    dept_description = models.TextField()
