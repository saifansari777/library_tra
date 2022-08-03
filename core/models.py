from datetime import datetime
from django.db import models

# Create your models here.

class Book(models.Model):

    status_choices = (
        ("BORROWED", "BORROWED"),
        ("AVAILABLE", "AVAILABLE")
    )
    name = models.CharField(max_length=255)
    author = models.CharField(max_length=255)
    description = models.TextField()
    status = models.CharField(
                            max_length = 20,
                            choices=status_choices
                            )
    created_at = models.DateField(default=datetime.now)
    updated_at = models.DateField(default=datetime.now)
    
