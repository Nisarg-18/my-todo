from datetime import datetime
from django.db import models
from ckeditor.fields import RichTextField

# Create your models here.
class Todo(models.Model):
    title=models.CharField(max_length=255)
    description=RichTextField()
    created_date=models.DateTimeField(default=datetime.now())

    def __str__(self):
        return self.title
