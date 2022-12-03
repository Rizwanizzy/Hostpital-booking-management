from django.db import models


# Create your models here.
# creating a table with name departments and its required fields
class departments(models.Model):
    dept_name = models.CharField(max_length=50)
    dept_description = models.TextField()
    dept_image = models.ImageField(upload_to='departments')

    # to display in admin dashboard with its name
    def __str__(self):
        return self.dept_name


# creating a table with name doctors and its required fields
class doctors(models.Model):
    doc_name = models.CharField(max_length=50)
    doc_spec = models.CharField(max_length=50)
    dep_name = models.ForeignKey(departments, on_delete=models.CASCADE)
    doc_image = models.ImageField(upload_to='doctors')

    # to display in admin dashboard with its name and specialization
    def __str__(self):
        return "Dr." + self.doc_name + " " + "( " + self.doc_spec + " )"


# creating a table with name booking and its required fields
class booking(models.Model):
    p_name = models.CharField(max_length=50)
    p_phone = models.CharField(max_length=13)
    p_email = models.EmailField(max_length=50)
    doc_name = models.ForeignKey(doctors, on_delete=models.CASCADE)
    booking_date = models.DateField()
    booked_on = models.DateField(auto_now=True)
