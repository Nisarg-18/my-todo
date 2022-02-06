from datetime import datetime
from django.db import models
from ckeditor.fields import RichTextField

# Create your models here.
class Todo(models.Model):
    priority_choices=(
        ('Urgent','Urgent'),
        ('EOD','EOD'),
        ('No Deadline','No Deadline'),
    )
    title=models.CharField(max_length=255)
    description=RichTextField()
    priority=models.CharField(max_length=100, choices=priority_choices)
    created_date=models.DateTimeField(default=datetime.now())

    def __str__(self):
        return self.title
