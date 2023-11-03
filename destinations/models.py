from django.db import models

# Create your models here.
# destinations/models.py
from django.db import models

class Destination(models.Model):
    name = models.CharField(max_length=100)
    description = models.TextField()
    location = models.CharField(max_length=100, default='Unknown')
    image = models.ImageField(upload_to='destinations/images/')
    # Add more fields as needed

class ProgramDetails(models.Model):
    destination = models.ForeignKey(Destination, on_delete=models.CASCADE)
    program_name = models.CharField(max_length=100)
    program_description = models.TextField()
    # Add more fields as needed

class ProgramDates(models.Model):
    program = models.ForeignKey(ProgramDetails, on_delete=models.CASCADE)
    start_date = models.DateField()
    end_date = models.DateField()
    # Add more fields as needed

class ProgramFees(models.Model):
    program = models.ForeignKey(ProgramDetails, on_delete=models.CASCADE)
    tuition = models.DecimalField(max_digits=10, decimal_places=2)
    housing = models.DecimalField(max_digits=10, decimal_places=2)
    # Add more fields as needed
