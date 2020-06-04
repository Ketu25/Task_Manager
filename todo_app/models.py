from django.db import models
from django.urls import reverse
# Create your models here.

class Todo(models.Model):
    items = models.CharField(max_length=2560)

    def __str__(self):
        return self.items

    def get_absolute_url(self):
        return reverse('todo_app:details', kwargs={'pk':self.pk})

