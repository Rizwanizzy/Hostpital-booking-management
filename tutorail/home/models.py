from django.db import models


# Create your models here.
class departments(models.Model):
    dept_name = models.CharField(max_length=50)
    dept_description = models.TextField()

    def __str__(self):
        return self.dept_name


class doctors(models.Model):
    doc_name = models.CharField(max_length=50)
    doc_spec = models.CharField(max_length=50)
    dep_name = models.ForeignKey(departments, on_delete=models.CASCADE)
    doc_image = models.ImageField(upload_to='doctors')
