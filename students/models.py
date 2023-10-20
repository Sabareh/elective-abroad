from django.db import models

# Create your models here.
# students/models.py
from django.db import models

class StudentProfile(models.Model):
    first_name = models.CharField(max_length=100)
    last_name = models.CharField(max_length=100)
    email = models.EmailField()

    def __str__(self):
        return self.first_name + ' ' + self.last_name
  

class ApplicationForm(models.Model):
    student = models.ForeignKey(StudentProfile, on_delete=models.CASCADE)
    department = models.CharField(max_length=100)
    destination = models.ForeignKey('destinations.Destination', on_delete=models.PROTECT)
    application_date = models.DateTimeField(auto_now_add=True)
    status = models.CharField(max_length=100, default='Pending')
    comment = models.TextField(blank=True, null=True)
    def __str__(self):
        return self.student.first_name + ' ' + self.student.last_name + ' ' + self.destination.name





