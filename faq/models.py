from django.db import models

# Create your models here.
from django.db import models

class FAQ(models.Model):
    question = models.CharField(max_length=255)
    answer = models.TextField()
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)
    class Meta:
        db_table = 'faq'

    def __str__(self):
        return self.question
    
    def __unicode__(self):
        return self.question
    
