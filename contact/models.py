from django.db import models

class Contact(models.Model):
    first_name = models.CharField(max_length=100)
    last_name = models.CharField(max_length=100)
    email = models.EmailField()
    phone = models.CharField(max_length=20)
    institution = models.CharField(max_length=100)
    program = models.CharField(max_length=100)
    how_did_you_hear = models.CharField(max_length=100)
    inquiry = models.TextField()
    
    # Add fields for passport, CV, and transcript uploads
    passport = models.FileField(upload_to='uploads/passports/', blank=True, null=True)
    cv = models.FileField(upload_to='uploads/cvs/', blank=True, null=True)
    transcript = models.FileField(upload_to='uploads/transcripts/', blank=True, null=True)

    def __str__(self):
        return f'{self.first_name} {self.last_name}'





