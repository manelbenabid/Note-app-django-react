from django.db import models

# Create your models here.

class Note(models.Model):
    body = models.TextField(null=True, blank = True)
    updated = models.DateTimeField(auto_now = True) #takes updated time stamp
    created = models.DateTimeField(auto_now_add=True) # takes one timestamp at creation


    def __str__(self):
        return self.body[0:50]