from django.db import models

# Create your models here.

CHOICES = (
    ('High', 'High'),
    ('Medium', 'Medium'),
    ('Low', 'Low'),
)

class Todo(models.Model):
    title = models.CharField(max_length=30)
    description = models.CharField(max_length=200, null=True, blank=True)
    priority = models.CharField(max_length=6, choices=CHOICES)
    complete = models.BooleanField(default=False)
    created = models.DateTimeField(auto_now_add=True)
    updated = models.DateTimeField(auto_now=True)

    def __str__(self):
        return self.title
