from django.db import models

# Create your models here.

class Comment(models.Model):
    content = models.TextField(max_length=255)
    first_name = models.CharField(max_length=255)
    email = models.EmailField(max_length=255 )
    
    def __str__(self):
        return self.name